---
name: mindshift-accessibility
description: "For MindShift and its products only. Use when working on UI interactions or component changes."
---
# Accessibility

## Trigger
Ui interactions or component changes.

## Procedure
Check semantic markup, keyboard, focus, contrast, screen readers, reduced motion and errors.

## Required output
WCAG-oriented checklist, automated and manual test results.

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

## MindShift dropdown invariant (owner correction, 2026-10-29)

For any select or dropdown trigger, explicitly review the arrow placement instead of accepting browser defaults:
- Use exactly one downward chevron, vertically centered at logical inline-end (left in RTL, right in LTR). Never mirror a downward chevron horizontally or position it with a fixed left/right rule shared by both directions.
- Reserve at least 44px inline-end padding for the icon slot and keep the chevron 12–16px inside the border. The label and selected value must never touch or overlap the arrow.
- With a custom chevron, remove the native arrow (`appearance: none`); make the decorative icon `aria-hidden` and `pointer-events: none`. With Radix Select, use one Select.Icon and equivalent logical spacing. Do not stack a native arrow and a custom icon.
- Preserve a visible focus state, a labeled control, keyboard navigation, and a minimum 44px trigger height.
- Before delivery, inspect both Arabic RTL and English LTR with long selected text on narrow and desktop widths. A select with an unreviewed, duplicated, clipped, edge-hugging, or text-overlapping arrow is unfinished.

- Inspect shared/global select CSS before adding a chevron. A background SVG must explicitly set `background-repeat: no-repeat`, `background-size`, and logical direction-aware placement. Exclude selects with their own icon from that background rule; repeated background arrows are a blocking visual defect.
