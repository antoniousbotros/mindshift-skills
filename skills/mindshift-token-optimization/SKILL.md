---
name: mindshift-token-optimization
description: "For MindShift and its products only. Use when context bloat, agent expense, long tasks."
---
# Token Optimization

## Trigger
Context bloat, agent expense, long tasks.

## Inputs to inspect (targeted)
- Task goal, affected users and acceptance criteria.
- Relevant project config, source files, interfaces and current tests.
- Available telemetry, constraints and existing decisions; mark missing evidence.

## Procedure
Establish baseline tokens, task success and retries. Use progressive disclosure, targeted grep, file-range reads, bounded outputs, compact checkpoints and caching where supported. Compare savings against quality and regression rates.

## Required output
Token budget; retrieval plan; before/after measurements; failure escalation.

## Quality gates
- Confirm the requested behavior and acceptance criteria before coding.
- Run available relevant checks; state exactly what ran and what did not.
- Explain risks, alternatives and rollback when material.
- Decision gate: classify the task as trivial, standard or high-risk. For standard and high-risk work, weigh benefit, cost, alternatives and reversibility, and get approval before price/plan, deletion, production schema, broad-permission, payment-logic or major UX-flow changes.
- Release gate: run tests and checks for what changed, cover security and data safety where affected, keep a rollback for high-impact changes, and report exactly what ran.

## Guardrails
- Do not skip security checks or tests to save tokens.
- Do not claim tests, research, metrics or deployment results that were not observed.
- Read relevant files only; avoid dumping the full repository into context.

## Evaluation
A second engineer can reproduce the decision, inspect evidence, and verify the acceptance criteria.

## MindShift scope
Apply this skill only to MindShift and its products. Follow the user’s current instructions and existing project rules; do not introduce Wasl, Stripe, or refund automation without a new explicit request.
