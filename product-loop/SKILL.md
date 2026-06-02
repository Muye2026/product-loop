---
name: product-loop
description: Drive a small hardware product from idea to design pack, with research-backed component and module selection before industrial design, plus explicit branching for CAD-capable and non-CAD environments. Use when Codex needs to research comparable products, shortlist plausible modules or components, explore physical product directions, refine concept renders, translate visuals into appearance and structure specs, emit a CAD-ready design pack, or hand off a product concept for downstream modeling. Best suited for small consumer electronics, desktop hardware, and lightweight robotic accessories; not for production-grade DFM, tooling, tolerance stacks, or large mechanical systems.
---

# Product Loop

Run a staged workflow that turns a hardware product brief into reusable design artifacts. Keep the skill explicit about environment capability, checkpoints, outputs, and stop conditions.

## Interaction Mode

Choose one interaction mode before Phase 1. Read [references/checkpoint-mode.md](references/checkpoint-mode.md).

- `checkpointed`: default for new product ideas. Stop at each decision gate and wait for user selection or approval.
- `auto`: only use when the user explicitly asks for an end-to-end package without intermediate approval.

Default to `checkpointed` when the user is starting from a new idea, asks for exploration, or has not explicitly authorized autonomous selection.

Never auto-select a direction, module architecture, render variant, or final concept when multiple viable options exist unless the user explicitly authorizes autonomous selection.

## Workflow

Follow this flow in order:

1. Run `Phase 0: Environment Check`.
2. Run `Phase 1: Brief Clarification`.
3. Run `Phase 1.5: Module Architecture Framing` when needed.
4. Run `Phase 1.6: Research-backed Component Selection`.
5. Run `Phase 2: Direction Exploration`.
6. Run `Phase 3: Visual Convergence`.
7. Run `Phase 4: Design Translation`.
8. Run `Phase 5: CAD Loop or Handoff`.

Do not skip a phase unless the user already provides the required artifact from an earlier phase. In that case, resume from the earliest missing artifact.

## Phase 0: Environment Check

Determine the execution mode before doing design work. Read [references/environment-check.md](references/environment-check.md).

Inspect these capability buckets:

- Image generation: confirm whether the session can generate or iterate renders.
- Research: confirm whether current context supports comparable-product and component-reference research.
- CAD: confirm whether the environment has a usable CAD workflow, a modeling CLI, or a local script pipeline.
- Inputs: confirm whether the user provided a brief, constraints, reference images, component assumptions, and component dimensions.

Declare exactly one execution mode:

- `full`: CAD-capable environment; continue through CAD iteration.
- `spec-only`: no CAD environment; stop at design pack plus review artifacts.
- `handoff`: environment or inputs are incomplete; emit a downstream handoff package.

State the selected mode explicitly before moving on.

## Phase 1: Brief Clarification

Normalize the product brief into a stable input contract. Read [references/brief-template.md](references/brief-template.md).

Capture or confirm:

- product goal
- target user
- use scenario
- primary functions
- component list or module assumptions
- size, mounting, and power constraints
- interaction constraints
- style intent
- known risks and unknowns

If key constraints are missing, ask for them or mark them as assumptions. Do not jump to final imagery with an underspecified brief.

## Phase 1.5: Module Architecture Framing

When key module or component architecture is still open, frame the choices before direction exploration. Read [references/module-architecture.md](references/module-architecture.md).

Trigger this phase only when at least one unresolved module decision would materially change:

- overall silhouette or body proportion
- front-face layout
- opening, port, or interface zoning
- mounting logic
- internal stacking or cooling path
- stability, balance, or service access

Typical trigger categories include:

- display strategy
- sensor or camera strategy
- audio strategy
- mounting strategy
- power strategy
- thermal strategy
- board topology or module split

Do not trigger this phase for trivial part-level uncertainty that does not materially affect industrial design or structure.

When triggered, provide 2-4 viable options for each unresolved architecture dimension. For each option, provide:

- option name
- what it means physically
- impact on appearance
- impact on structure
- main risk
- what kinds of product directions it enables

### Gate 0.5: Module Selection

In `checkpointed` mode:

- output only `Module Options`
- do not continue into direction exploration yet
- do not auto-select a module architecture
- ask the user to:
  - choose one option for each critical unresolved module dimension, or
  - authorize a narrowed recommendation set for the next pass
- stop and wait

In `auto` mode, you may recommend and continue with one architecture set, but you must state why it was selected and which downstream constraints it fixed.

## Phase 1.6: Research-backed Component Selection

Before direction exploration, translate the product goal and module architecture into plausible real-world component and packaging constraints. Read [references/component-selection.md](references/component-selection.md).

When research access is available, inspect comparable products, teardown notes, marketplace listings, maker modules, and manufacturer or distributor references. Use a globally balanced source mix unless the user asks for a specific market.

Emit:

- `Reference Cases`
- `Component Requirements`
- `Candidate Components`
- `Selected or Assumed Components`
- `Packaging Constraints`
- `Sourcing Risks`

Default depth:

- choose module-level solutions first
- include 2-4 concrete candidate parts, modules, or structural material options for each critical module
- capture package size, interface, mounting, thermal, service, and sourcing implications when available
- mark uncertain dimensions as assumptions instead of pretending they are verified

In `checkpointed` mode, recommend a component set and continue into Phase 2 unless there is no feasible component path, the options conflict with hard constraints, or the user explicitly asks to approve component selection first.

Do not treat industrial design as free-form styling. Direction exploration must inherit the selected or assumed component envelopes, visible module constraints, mounting logic, and sourcing risks from this phase.

## Phase 2: Direction Exploration

Generate 2-4 distinct directions, not 2-4 cosmetic variants of the same direction.

For each direction, provide:

- a short name
- 3-6 keywords
- a one-paragraph concept summary
- why the direction fits the brief
- structural plausibility notes
- main risks
- what would need validation before CAD
- best-fit use case or product posture

Favor directions that remain buildable after selected or assumed components, packaging constraints, component envelopes, and mounting logic are applied.

### Gate A: Direction Selection

In `checkpointed` mode:

- output only `Concept Directions`
- do not generate final renders yet
- do not auto-select a direction
- ask the user to either:
  - select 1 direction to continue, or
  - shortlist up to 2 directions for another comparison round
- stop and wait

In `auto` mode, you may recommend and continue with one direction, but you must state why it was selected.

## Phase 3: Visual Convergence

Refine only the selected direction. Keep all hard constraints stable while iterating visuals.

When driving image work:

- vary emphasis, proportion, front-face layout, and silhouette intentionally
- preserve mounting logic and component plausibility
- reject aesthetic drift that breaks usability or structure
- treat renders as visual targets, not geometry truth

### First Pass: Render Variants

In `checkpointed` mode, the first pass of Phase 3 must produce 3-4 render variants within the selected direction. These must vary along meaningful axes such as:

- silhouette emphasis
- front-face hierarchy
- CMF mood
- hardware expression level
- home vs. professional product posture

Do not produce a final hero render on the first pass.

### Gate B: Variant Selection

In `checkpointed` mode:

- output only `Render Variants`
- ask the user to select one variant and list any adjustment notes
- stop and wait

### Second Pass: Near-Final Candidate

After the user selects a variant, refine it into a near-final candidate render set.

At the end of this pass, provide:

- the near-final candidate
- a short change summary
- unresolved visual questions

### Gate C: Render Freeze

In `checkpointed` mode:

- ask the user whether to freeze the candidate render and move into design translation
- do not enter `Phase 4` without approval unless the user explicitly authorizes autonomous continuation
- stop and wait

In `auto` mode, you may freeze the candidate render yourself and continue, but you must call out the unresolved visual questions.

## Phase 4: Design Translation

Translate the chosen visual direction into structured design artifacts. Do not write a loose summary. Read:

- [references/appearance-spec-template.md](references/appearance-spec-template.md)
- [references/structure-spec-template.md](references/structure-spec-template.md)
- [references/design-pack-schema.md](references/design-pack-schema.md)

Emit:

- `Appearance Spec`
- `Structure Spec`
- `Design Pack`
- `Review Report`

Translate visuals into executable constraints, including:

- proportion and overall envelope
- front, side, top, and rear zoning
- openings, ports, and button placement
- selected or assumed components
- component envelopes
- packaging constraints
- sourcing risks
- mounting strategy
- structure and manufacturability risks
- forbidden features
- acceptance checks

If the session is not in `full` mode, also emit a downstream handoff brief with [references/handoff-brief-template.md](references/handoff-brief-template.md).

## Phase 5: CAD Loop or Handoff

### Full Mode

Drive a parametric draft model from the design pack.

Use the design pack as the source of truth for:

- target envelope
- selected or assumed components
- component keep-outs
- packaging constraints
- mounting logic
- split strategy
- key style features
- acceptance checks

After each iteration, compare:

- render target vs. current geometry
- structure spec vs. current layout
- design pack constraints vs. current model

Record only actionable deltas:

- appearance delta
- layout delta
- structure delta
- manufacturing-risk delta

Emit:

- `CAD Iteration Inputs`
- `Parametric Draft Model`
- `CAD Iteration Report`

### Spec-Only or Handoff Mode

Stop after creating:

- `Design Pack`
- `Handoff Brief`
- `Review Report`

Make the handoff unambiguous for a downstream modeler:

- modeling target
- envelope and critical dimensions
- selected or assumed components
- packaging constraints and sourcing risks
- suggested part split
- priority constraints
- open questions

## Output Contract

Produce only the artifacts for the current approved phase.

### Checkpointed Mode

- After `Phase 1.5` when triggered: `Module Options`
- During `Phase 1.6`: produce `Reference Cases`, `Component Requirements`, `Candidate Components`, `Selected or Assumed Components`, `Packaging Constraints`, and `Sourcing Risks`; continue into Phase 2 unless component selection is infeasible or user approval is requested.
- After `Phase 2`: `Concept Directions` plus the Phase 1.6 component-selection artifacts that constrained those directions
- After first `Phase 3` pass: `Render Variants`
- After final `Phase 3` approval: `Render Set`
- After `Phase 4`: `Appearance Spec`, `Structure Spec`, `Design Pack`, `Review Report`
- After `Phase 4` in non-`full` modes: also `Handoff Brief`
- After `Phase 5` in `full` mode: `CAD Iteration Inputs`, `Parametric Draft Model`, `CAD Iteration Report`

### Auto Mode

You may produce the full end-to-end package in one run when the user explicitly asks for it.

Use `execution_mode` inside the design pack so downstream tools or collaborators can see which path was used.

## References

Use the reference files selectively:

- `checkpoint-mode.md`: choose the interaction style and obey phase gates
- `brief-template.md`: gather or normalize the brief
- `module-architecture.md`: decide whether module selection is needed and frame the options
- `component-selection.md`: research comparable products and shortlist plausible modules or components before styling
- `environment-check.md`: choose the execution mode
- `design-pack-schema.md`: define the machine-readable design pack
- `appearance-spec-template.md`: write visual and CMF constraints
- `structure-spec-template.md`: write structure and layout constraints
- `handoff-brief-template.md`: prepare non-CAD delivery
- `review-rubric.md`: assess quality and readiness
- `use-cases.md`: inspect examples and non-goals

## Rules

- Prefer explicit assumptions over silent guessing.
- Keep the design pack structured enough for scripts and downstream modeling.
- Base industrial design on researched or assumed component constraints, not on pure appearance.
- Treat image outputs as visual targets, not as geometry truth.
- Stop at the appropriate boundary for the execution mode.
- Stop at the appropriate checkpoint for the interaction mode.
- Refuse to imply production readiness when only a concept, spec, or draft model exists.
