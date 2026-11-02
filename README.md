# MindShift skills

These are the agent skills MindShift uses with Claude Code and Codex across its products. Each skill is one `SKILL.md`: a trigger, what to inspect, a procedure, the required output, quality gates, guardrails and how to evaluate the result.

There are two parts:

- **[`skills/`](skills/)**: 40 MindShift skills covering engineering, quality, security, product, growth, design and localisation.
- **[`figma/`](figma/)**: an installer for 16 of Figma's official skills, with a vetted MindShift overlay. Figma's text isn't stored here. The installer downloads it from Figma at a pinned, hash-checked commit.

## Install the MindShift skills

Clone the repo, then copy (or symlink) the skill folders into your agent's skills directory:

```bash
git clone https://github.com/antoniousbotros/mindshift-skills.git
cp -R mindshift-skills/skills/mindshift-* ~/.claude/skills/
cp -R mindshift-skills/skills/mindshift-* ~/.codex/skills/
```

Start a new session afterwards so the agent picks them up. Existing skills with the same names are overwritten by `cp`, so check first if you've edited local copies.

## Install the Figma skills

```bash
python3 mindshift-skills/figma/install_figma_skills.py
python3 mindshift-skills/figma/install_figma_skills.py --apply
python3 mindshift-skills/figma/install_figma_skills.py --apply --target ~/.claude/skills --target ~/.codex/skills
```

The first command is a dry run, which is the default. `--apply` does the following:

1. Downloads the 95 upstream files from [`figma/mcp-server-guide`](https://github.com/figma/mcp-server-guide).
2. Checks each file against [`figma/upstream.sha256`](figma/upstream.sha256), and stops without installing anything if any file differs.
3. Writes `mindshift-figma-*` skills in this collection's format, adding the guardrails and narrowed triggers in [`figma/overlay.json`](figma/overlay.json).

It never runs downloaded content, uses only the Python standard library, and refuses to replace existing skills unless you pass `--force`. How each skill was vetted is in [`figma/VETTING.md`](figma/VETTING.md).

The Figma skills need the Figma MCP server connected in your agent.

## Skills

| Skill | Use when |
|---|---|
| [`mindshift-accessibility`](skills/mindshift-accessibility/SKILL.md) | Use when working on UI interactions or component changes. |
| [`mindshift-agent-architecture`](skills/mindshift-agent-architecture/SKILL.md) | Use when working on AI agents, tools, permissions or automation. |
| [`mindshift-ai-research`](skills/mindshift-ai-research/SKILL.md) | Use when new ai models, tools and r&d. |
| [`mindshift-analytics`](skills/mindshift-analytics/SKILL.md) | Use when events, funnels, cohorts, attribution. |
| [`mindshift-api-design`](skills/mindshift-api-design/SKILL.md) | Use when working on new endpoints or external integrations. |
| [`mindshift-architecture`](skills/mindshift-architecture/SKILL.md) | Use when system design, major refactors, new services. |
| [`mindshift-backend`](skills/mindshift-backend/SKILL.md) | Use when api, jobs, webhooks, business logic. |
| [`mindshift-billing`](skills/mindshift-billing/SKILL.md) | Use when subscriptions, payments, credits. |
| [`mindshift-code-review`](skills/mindshift-code-review/SKILL.md) | Use when working on pull request or code quality audit. |
| [`mindshift-cost-optimization`](skills/mindshift-cost-optimization/SKILL.md) | Use when working on infrastructure, AI API or SaaS spend. |
| [`mindshift-customer-retention`](skills/mindshift-customer-retention/SKILL.md) | Use when working on churn, engagement or lifecycle messaging. |
| [`mindshift-cybersecurity`](skills/mindshift-cybersecurity/SKILL.md) | Use when auth, access, secrets, threats, audits. |
| [`mindshift-data-privacy`](skills/mindshift-data-privacy/SKILL.md) | Use when working on personal data, consent, deletion or data export. |
| [`mindshift-database`](skills/mindshift-database/SKILL.md) | Use when schema, sql, supabase, migrations. |
| [`mindshift-devops`](skills/mindshift-devops/SKILL.md) | Use when ci/cd, deployments, infrastructure. |
| [`mindshift-disaster-recovery`](skills/mindshift-disaster-recovery/SKILL.md) | Use when working on backup, recovery or reliability. |
| [`mindshift-documentation`](skills/mindshift-documentation/SKILL.md) | Use when working on docs, runbooks or architectural explanation. |
| [`mindshift-experimentation`](skills/mindshift-experimentation/SKILL.md) | Use when working on A/B test or product hypothesis. |
| [`mindshift-feature-flags`](skills/mindshift-feature-flags/SKILL.md) | Use when working on gradual rollout or experiments. |
| [`mindshift-frontend`](skills/mindshift-frontend/SKILL.md) | Use when react, next.js, web ui. |
| [`mindshift-growth`](skills/mindshift-growth/SKILL.md) | Use when working on activation, conversion, retention or funnels. |
| [`mindshift-incident-response`](skills/mindshift-incident-response/SKILL.md) | Use when working on outage, degradation or production issue. |
| [`mindshift-localization`](skills/mindshift-localization/SKILL.md) | Use when working on countries, currencies, languages or RTL. |
| [`mindshift-migration-safety`](skills/mindshift-migration-safety/SKILL.md) | Use when working on schema/data/backfill or major platform move. |
| [`mindshift-multi-tenant-isolation`](skills/mindshift-multi-tenant-isolation/SKILL.md) | Use when working on tenant queries, RLS or shared infrastructure. |
| [`mindshift-observability`](skills/mindshift-observability/SKILL.md) | Use when working on logs, metrics, traces or monitoring. |
| [`mindshift-payment-security`](skills/mindshift-payment-security/SKILL.md) | Use when working on payment provider or money movement. |
| [`mindshift-performance`](skills/mindshift-performance/SKILL.md) | Use when working on latency, throughput or slow app. |
| [`mindshift-pricing`](skills/mindshift-pricing/SKILL.md) | Use when plans, bundles, credits, monetization. |
| [`mindshift-product-strategy`](skills/mindshift-product-strategy/SKILL.md) | Use when feature requests, onboarding changes, roadmap prioritization. |
| [`mindshift-prompt-engineering`](skills/mindshift-prompt-engineering/SKILL.md) | Use when prompts, system instructions, ai behavior regressions. |
| [`mindshift-refactoring`](skills/mindshift-refactoring/SKILL.md) | Use when working on restructure or clean existing code. |
| [`mindshift-release-management`](skills/mindshift-release-management/SKILL.md) | Use when working on shipping features, versions or migrations. |
| [`mindshift-saas-architecture`](skills/mindshift-saas-architecture/SKILL.md) | Use when working on multi-tenant or subscription platform changes. |
| [`mindshift-seo-geo`](skills/mindshift-seo-geo/SKILL.md) | Use when working on SEO, structured data or AI discovery. |
| [`mindshift-testing`](skills/mindshift-testing/SKILL.md) | Use when qa, regressions, feature completion. |
| [`mindshift-token-optimization`](skills/mindshift-token-optimization/SKILL.md) | Use when context bloat, agent expense, long tasks. |
| [`mindshift-typography`](skills/mindshift-typography/SKILL.md) | Use when arabic/english font decisions. |
| [`mindshift-ui-design`](skills/mindshift-ui-design/SKILL.md) | Use when visual interfaces, design systems. |
| [`mindshift-ux-research`](skills/mindshift-ux-research/SKILL.md) | Use when onboarding, forms, user journeys, retention. |

### Figma (installed by `figma/install_figma_skills.py`)

`mindshift-figma-use` (load before every `use_figma` call), `-use-motion`, `-use-figjam`, `-use-slides`, `-create-new-file`, `-generate-design`, `-generate-library`, `-generate-diagram`, `-design-to-code`, `-implement-motion`, `-swiftui`, `-code-connect`, `-code-workflows`, `-spec`, `-generative-plugins`, `-shaders`.

## Scope

Every skill is written for MindShift and its products. Its description says so, so agents don't apply it to unrelated work. To reuse these elsewhere, edit the description and the closing "MindShift scope" section.

## License

The MindShift skills and the installer are under the [MIT License](LICENSE). The Figma skills belong to Figma and are not included. The installer fetches them from Figma's public repository, under Figma's terms.
