# Checkpoint Mode

`product-loop` supports two interaction styles.

## 1. `checkpointed`

Use this by default for new product ideas.

The goal is not to maximize autonomy. The goal is to preserve human decision authority at the moments that actually matter.

### Required stop points

#### Gate 0.5: Module Selection

When `Phase 1.5` is triggered, output only module architecture options.

The agent must not:

- continue into concept directions yet
- auto-select one architecture set
- hide a major module decision inside a later design direction

The agent must ask the user to:

- choose the critical module options, or
- explicitly authorize a narrowed recommendation set

#### Gate A: Direction Selection

After `Phase 2`, output only concept directions.

The agent must not:

- generate final renders
- auto-select one direction
- collapse multiple viable directions into one final answer

The agent must ask the user to:

- pick 1 direction to continue, or
- shortlist up to 2 directions for another comparison round

#### Gate B: Variant Selection

After the first pass of `Phase 3`, output only 3-4 render variants within the chosen direction.

The agent must not:

- present the first render pass as final
- move into design translation
- silently choose a preferred render variant

The agent must ask the user to:

- select one variant
- optionally list change notes

#### Gate C: Render Freeze

After refining the selected variant into a near-final candidate, stop again.

The agent must ask the user whether to:

- freeze the render and move into design translation, or
- continue another render-refinement round

### Practical intent

This mode is appropriate when the user wants:

- exploration before commitment
- explicit architecture choices before styling
- researched component assumptions before styling
- multiple design directions
- visible decision points
- collaborative narrowing, not agent-side auto-closure

## 2. `auto`

Use only when the user explicitly asks for an end-to-end package without intermediate approval.

This mode allows the agent to:

- recommend and select a module architecture set
- recommend and select a provisional component set
- recommend and select one direction
- continue through render convergence without waiting
- emit the final document package in one run

Even in `auto` mode, the agent must still:

- state why architecture and direction were selected
- state why provisional components were selected
- call out assumptions
- separate confirmed facts from assumptions
- avoid implying production readiness

## Invocation guidance

Typical `checkpointed` requests sound like:

- "Give me 3 different directions first, then wait for my choice."
- "Do not auto-select a concept for me."
- "Show several variants inside one direction before giving me a final render."
- "Let me choose the module strategy first, then continue."
- "Show me component choices before industrial design."

`Phase 1.6` does not create a required stop by default. In checkpointed mode, the agent should recommend a provisional component set and continue unless no feasible candidate satisfies hard constraints, the component choice materially changes architecture, or the user asks to approve components first.

Typical `auto` requests sound like:

- "Run end to end and give me the complete package."
- "You can choose the best direction yourself and continue."

## Override rule

If the user explicitly asks to stop at a checkpoint, that instruction overrides any default tendency to continue.
