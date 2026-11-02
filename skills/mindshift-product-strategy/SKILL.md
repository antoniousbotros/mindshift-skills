---
name: mindshift-product-strategy
description: "For MindShift and its products only. Use when feature requests, onboarding changes, roadmap prioritization."
---
# Product Strategy

## Trigger
Feature requests, onboarding changes, roadmap prioritization.

## Inputs to inspect (targeted)
- Task goal, affected users and acceptance criteria.
- Relevant project config, source files, interfaces and current tests.
- Available telemetry, constraints and existing decisions; mark missing evidence.

## Procedure
Define user segment, job-to-be-done, baseline funnel, constraints and non-goals. Identify 2 alternatives including do-nothing. Estimate directional impact on activation, retention, revenue, support load, and complexity. Label assumptions; recommend smallest measurable experiment.

## Required output
Problem statement; option matrix; primary metric + guardrail; decision and experiment design.

## Quality gates
- Confirm the requested behavior and acceptance criteria before coding.
- Run available relevant checks; state exactly what ran and what did not.
- Explain risks, alternatives and rollback when material.
- Decision gate: classify the task as trivial, standard or high-risk. For standard and high-risk work, weigh benefit, cost, alternatives and reversibility, and get approval before price/plan, deletion, production schema, broad-permission, payment-logic or major UX-flow changes.
- Release gate: run tests and checks for what changed, cover security and data safety where affected, keep a rollback for high-impact changes, and report exactly what ran.

## Guardrails
- Do not fabricate benchmarks, user research or conversion lifts.
- Do not claim tests, research, metrics or deployment results that were not observed.
- Read relevant files only; avoid dumping the full repository into context.

## Evaluation
A second engineer can reproduce the decision, inspect evidence, and verify the acceptance criteria.

## MindShift scope
Apply this skill only to MindShift and its products. Follow the user’s current instructions and existing project rules; do not introduce Wasl, Stripe, or refund automation without a new explicit request.
