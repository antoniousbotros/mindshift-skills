---
name: mindshift-api-design
description: "For MindShift and its products only. Use when working on new endpoints or external integrations."
---
# Api Design

## Trigger
New endpoints or external integrations.

## Procedure
Use consistent resources and errors, auth scopes, pagination, versioning, rate limits and contract compatibility.

## Required output
OpenAPI contract, sample requests, compatibility tests.

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
