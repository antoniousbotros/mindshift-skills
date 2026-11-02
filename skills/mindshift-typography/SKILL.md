---
name: mindshift-typography
description: "For MindShift and its products only. Use when arabic/english font decisions."
---
# Typography

## Trigger
Arabic/English font decisions.

## Inputs to inspect (targeted)
- Task goal, affected users and acceptance criteria.
- Relevant project config, source files, interfaces and current tests.
- Available telemetry, constraints and existing decisions; mark missing evidence.

## Procedure
Check licensing, Arabic glyph coverage, numeral handling, font loading and fallback, weights, line height and mixed-direction text. Compare real device rendering and CLS impacts.

## Required output
Font stack; type scale; licensing and performance notes; RTL samples.

## Quality gates
- Confirm the requested behavior and acceptance criteria before coding.
- Run available relevant checks; state exactly what ran and what did not.
- Explain risks, alternatives and rollback when material.
- Decision gate: classify the task as trivial, standard or high-risk. For standard and high-risk work, weigh benefit, cost, alternatives and reversibility, and get approval before price/plan, deletion, production schema, broad-permission, payment-logic or major UX-flow changes.
- Release gate: run tests and checks for what changed, cover security and data safety where affected, keep a rollback for high-impact changes, and report exactly what ran.

## Guardrails
- Do not ship unlicensed fonts or assume Latin fonts support Arabic.
- Do not claim tests, research, metrics or deployment results that were not observed.
- Read relevant files only; avoid dumping the full repository into context.

## Evaluation
A second engineer can reproduce the decision, inspect evidence, and verify the acceptance criteria.

## MindShift scope
Apply this skill only to MindShift and its products. Follow the user’s current instructions and existing project rules; do not introduce Wasl, Stripe, or refund automation without a new explicit request.

## MindShift numeral preference
Owner preference (2026-10-29): use Western digits 0–9 in Arabic interfaces, including prices, balances, counters, percentages and dates. Keep Arabic wording and RTL layout. Use `ar-EG-u-nu-latn` or `numberingSystem: "latn"` with Intl; do not hardcode Arabic-Indic digits or rely on an Arabic locale's default numbering system.
