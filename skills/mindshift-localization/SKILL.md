---
name: mindshift-localization
description: "For MindShift and its products only. Use when working on countries, currencies, languages or RTL."
---
# Localization

## Trigger
Countries, currencies, languages or rtl.

## Procedure
Separate locale from region and billing currency; handle ICU formatting, translation keys, pluralization, RTL and fallback.

## Required output
Locale matrix, i18n keys, regional test cases.

## Guardrails
- Read only relevant repository files and source documentation.
- Never fabricate measurements, audits, tests or evidence.
- Prefer backward-compatible, reversible changes.
- Flag missing data and material risks explicitly.
- Decision gate: classify the task as trivial, standard or high-risk. For standard and high-risk work, weigh benefit, cost, alternatives and reversibility, and get approval before price/plan, deletion, production schema, broad-permission, payment-logic or major UX-flow changes.
- Release gate: run tests and checks for what changed, cover security and data safety where affected, keep a rollback for high-impact changes, and report exactly what ran.

## Evaluation
A reviewer can reproduce the decision, inspect implementation evidence, and verify acceptance criteria without relying on the agent's assertions.

## MindShift scope
Apply this skill only to MindShift and its products. Follow the user’s current instructions and existing project rules; do not introduce Wasl, Stripe, or refund automation without a new explicit request.

## MindShift numeral preference
Owner preference (2026-10-29): use Western digits 0–9 in Arabic interfaces, including prices, balances, counters, percentages and dates. Keep Arabic wording and RTL layout. Use `ar-EG-u-nu-latn` or `numberingSystem: "latn"` with Intl; do not hardcode Arabic-Indic digits or rely on an Arabic locale's default numbering system.
