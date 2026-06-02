# Use Cases

## Good Fits

Use `product-loop` for requests such as:

- "Turn this desktop hardware idea into three industrial design directions."
- "Give me several reference directions first, and let me choose before you render anything final."
- "Let me choose the module strategy first, then give me design directions."
- "Research comparable products and likely modules before creating industrial design directions."
- "For this parking number plate idea, compare display, privacy, mounting, illumination, and power options before styling."
- "Use these component assumptions to create concept directions and a CAD-ready design pack."
- "We already have a chosen render; extract appearance and structure specs."
- "We do not have CAD installed, but we still need a clean handoff package for a modeler."
- "Compare the current draft model against the approved direction and summarize the next geometry changes."

## Checkpointed Examples

Use `checkpointed` mode for requests such as:

- "Show me the critical module choices first and stop for selection."
- "Show me 3 distinct design directions and stop for selection."
- "Within the chosen direction, give me 4 render variants and wait for my pick."
- "Do not auto-select a final concept. I want to choose each step."

Expected behavior:

- If key module architecture is unresolved, stop after `Phase 1.5`.
- After `Phase 1.6`, continue with a recommended provisional component set unless the user asks to approve it or no feasible path exists.
- After `Phase 2`, stop at concept directions.
- After first `Phase 3` pass, stop at render variants.
- Before `Phase 4`, stop again for render freeze approval.

## Auto Examples

Use `auto` mode only for requests such as:

- "Run this product idea end to end and give me the complete package."
- "Pick the best module architecture and direction yourself and continue without waiting."

Expected behavior:

- The agent may continue across checkpoints.
- The agent must still explain why it selected the architecture and direction.
- The agent must still explain why it selected provisional components.

## Resume Cases

Resume from the earliest missing artifact:

- If the user already fixed the module strategy, skip `Phase 1.5`.
- If the user already provides component selections with usable envelopes, summarize them and skip or shorten `Phase 1.6`.
- If the user already has a render, skip direction exploration and move into design translation.
- If the user already has appearance and structure specs, emit a design pack and review report.
- If the user already has a draft CAD model, run the CAD review loop against the design pack.

## Non-Goals

Do not use this skill as the primary path for:

- large furniture or architectural systems
- production tooling documentation
- tolerance analysis
- direct mass-manufacturing release
- pure branding or marketing-page design work

## Boundary Reminder

This skill helps produce concept-ready and CAD-ready artifacts. It does not certify manufacturability or production readiness on its own.
