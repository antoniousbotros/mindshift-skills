#!/usr/bin/env python3
"""Install Figma's official agent skills with MindShift's vetted overlay.

Figma's skill text is not redistributed in this repository. This script downloads
it from github.com/figma/mcp-server-guide at the pinned commit in overlay.json,
checks every file against upstream.sha256, and writes collection-format copies
named mindshift-<skill> into each target skills directory.

Downloaded files are only read and rewritten as text. Nothing downloaded is
executed. Standard library only.

    python3 figma/install_figma_skills.py                      # dry run, ~/.claude/skills
    python3 figma/install_figma_skills.py --apply
    python3 figma/install_figma_skills.py --apply --target ~/.claude/skills --target ~/.codex/skills
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import sys
import tempfile
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
LINK = re.compile(r'(\]\((?:\.\./)+)(figma-[a-z-]+)(/)')
VETTING_URL = 'https://github.com/antoniousbotros/mindshift-skills/blob/main/figma/VETTING.md'
GATES = (
    '- Decision gate: classify the task as trivial, standard or high-risk. For standard and high-risk work, weigh benefit, '
    'cost, alternatives and reversibility, and get approval before price/plan, deletion, production schema, '
    'broad-permission, payment-logic or major UX-flow changes.\n'
    '- Release gate: run tests and checks for what changed, cover security and data safety where affected, keep a '
    'rollback for high-impact changes, and report exactly what ran.'
)


def load_hashes():
    hashes = {}
    for line in (HERE / 'upstream.sha256').read_text().splitlines():
        digest, path = line.split(None, 1)
        hashes[path.strip()] = digest
    return hashes


def fetch(overlay, hashes, dest):
    base = f"https://raw.githubusercontent.com/{overlay['upstream']}/{overlay['commit']}/skills/"
    for i, (path, digest) in enumerate(sorted(hashes.items()), 1):
        with urllib.request.urlopen(base + path, timeout=60) as resp:
            data = resp.read()
        got = hashlib.sha256(data).hexdigest()
        if got != digest:
            sys.exit(f'Hash mismatch for {path}: expected {digest}, got {got}. Nothing was installed.')
        out = dest / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
        print(f'  [{i}/{len(hashes)}] verified {path}', flush=True)


def relink(text, names):
    return LINK.sub(lambda m: m.group(1) + ('mindshift-' + m.group(2) if m.group(2) in names else m.group(2)) + m.group(3), text)


def demote(body):
    out, fence = [], False
    for line in body.split('\n'):
        if line.startswith('```'):
            fence = not fence
        if not fence and re.match(r'#{1,5} ', line):
            line = '#' + line
        out.append(line)
    return '\n'.join(out)


def build(name, src, odir, overlay):
    names = set(overlay['skills'])
    text = (src / 'SKILL.md').read_text(encoding='utf-8')
    fm, body = text[4:].split('\n---\n', 1)
    meta = dict((k.strip(), v.strip()) for k, _, v in (l.partition(':') for l in fm.split('\n')))
    desc = meta['description']
    inner = desc[1:-1] if desc.startswith('"') and desc.endswith('"') else desc.replace('"', '\\"')
    if name in overlay['desc_override']:
        inner = overlay['desc_override'][name].replace('"', '\\"')
        desc = '"' + inner + '"'
    trigger = json.loads(desc) if desc.startswith('"') else desc
    body = body.strip('\n')
    lines = body.split('\n')
    title = lines[0][2:].strip() if lines[0].startswith('# ') else name
    if lines[0].startswith('# '):
        body = '\n'.join(lines[1:]).strip('\n')
    for old, new in overlay['replace'].get(name, []):
        if old not in body:
            sys.exit(f'{name}: expected upstream text not found; overlay is out of date. Nothing was installed.')
        body = body.replace(old, new)
    body = relink(demote(body), names)
    x = overlay['per_skill'].get(name, {})
    guardrails = x.get('guardrails', []) + [
        "Do not delete, detach or restructure Figma content, or change files in the user's repository, beyond what the user asked for.",
        'Do not claim tests, research, metrics or deployment results that were not observed.',
        'Read relevant files only; avoid dumping the full repository into context.',
    ]
    changes = ['headings nested one level deeper under Procedure',
               'links to other Figma skills point to the local `mindshift-` copies'] + x.get('changes', [])
    pretty = ' '.join(w.capitalize() for w in name.replace('figma-', 'figma ').split())
    md = f'''---
name: mindshift-{name}
description: "For MindShift and its products only. {inner}"
---
# {pretty}

## Trigger
{trigger}

## Inputs to inspect (targeted)
- Task goal, the Figma file URL/key or node IDs involved, and acceptance criteria.
- Existing state before writing: what the Figma file (and, for code tasks, the repository) already contains and its conventions.
- Available Figma MCP tools in this session; mark any missing evidence.

## Procedure
Follow Figma's upstream `{name}` skill ("{title}"), kept as published below apart from the local changes listed under Source. Figma's skill names map to local skills with the `mindshift-` prefix (`figma-use` is `mindshift-figma-use`, and so on). Keep Figma's original names in any `skillNames` logging parameter.

{body}

## Required output
What changed (Figma node IDs, files or mappings), the evidence checked (returned data, metadata, screenshots, builds or tests that actually ran) and what was not verified.

## Quality gates
- Inspect before creating; match existing conventions.
- Confirm the requested behavior and acceptance criteria before writing; state exactly what was verified and what was not.
{GATES}

## Guardrails
''' + '\n'.join('- ' + g for g in guardrails) + f'''

## Evaluation
A second engineer can follow the returned IDs, files and evidence to confirm the result matches the acceptance criteria, with no unrequested changes.

## Source
Installed by mindshift-skills from Figma's official `{name}` skill (github.com/{overlay['upstream']}, commit `{overlay['commit'][:8]}`, hash-verified). Other files are verbatim upstream apart from cross-skill link paths. Local changes: ''' + '; '.join(changes) + f'''.
Vetting record: {VETTING_URL}

## MindShift scope
Apply this skill only to MindShift and its products. Follow the user’s current instructions and existing project rules; do not introduce Wasl, Stripe, or refund automation without a new explicit request.
'''
    odir.mkdir(parents=True)
    (odir / 'SKILL.md').write_text(md, encoding='utf-8')
    for f in sorted(src.rglob('*')):
        if f.is_file() and f.name != 'SKILL.md':
            dest = odir / f.relative_to(src)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if f.suffix == '.md':
                dest.write_text(relink(f.read_text(encoding='utf-8'), names), encoding='utf-8')
            else:
                shutil.copy2(f, dest)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--target', action='append', help='skills directory (repeatable; default ~/.claude/skills)')
    ap.add_argument('--apply', action='store_true', help='download and install (default is a dry run)')
    ap.add_argument('--force', action='store_true', help='replace existing mindshift-figma-* skills')
    a = ap.parse_args()
    overlay = json.loads((HERE / 'overlay.json').read_text())
    hashes = load_hashes()
    targets = [pathlib.Path(t).expanduser().resolve() for t in (a.target or ['~/.claude/skills'])]
    outs = {t: [t / ('mindshift-' + n) for n in overlay['skills']] for t in targets}
    existing = [str(p) for ps in outs.values() for p in ps if p.exists()]
    print(f"Figma skills: {len(overlay['skills'])} at {overlay['upstream']}@{overlay['commit'][:8]} ({len(hashes)} files)")
    print('Targets: ' + ', '.join(map(str, targets)) + f"; existing: {len(existing)}; mode: {'APPLY' if a.apply else 'DRY RUN'}")
    if existing and not a.force:
        print('Existing skills would be replaced:\n  ' + '\n  '.join(existing))
        if a.apply:
            sys.exit('Refusing to overwrite. Re-run with --force after reviewing.')
    if not a.apply:
        print('Dry run only. Re-run with --apply to download, verify and install.')
        return
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        fetch(overlay, hashes, tmp / 'upstream')
        for name in overlay['skills']:
            build(name, tmp / 'upstream' / name, tmp / 'built' / ('mindshift-' + name), overlay)
        for t, ps in outs.items():
            t.mkdir(parents=True, exist_ok=True)
            for p in ps:
                if p.exists():
                    shutil.rmtree(p)
                shutil.copytree(tmp / 'built' / p.name, p)
            print(f'Installed {len(ps)} skills into {t}')


if __name__ == '__main__':
    main()
