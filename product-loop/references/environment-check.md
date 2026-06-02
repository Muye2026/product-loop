# Environment Check

Run this phase before concept generation, document generation, or CAD work.

## Capability Buckets

Check four buckets:

1. `Image generation`
2. `Research access`
3. `CAD capability`
4. `Input completeness`

## What to Inspect

### Image generation

Confirm whether the current environment can:

- generate fresh concept renders
- refine an existing direction with prompt iteration
- accept a user-supplied reference image

### Research access

Confirm whether the current environment can:

- inspect similar products
- collect structure references
- inspect comparable product listings, teardown notes, and application cases
- inspect module or component references from current suppliers or distributors
- cite current product references when needed

### CAD capability

Confirm whether the current environment has at least one of:

- a usable CAD application
- a compatible CAD CLI
- a local parametric modeling script pipeline
- a stable export-and-review loop for geometry

Do not require a specific CAD brand. Check for capability, not for a logo.

### Input completeness

Confirm whether the session already has:

- a product brief or an equivalent artifact
- component assumptions
- component-selection assumptions or current candidate references
- target envelope or dimensions
- mounting or placement logic
- any reference images or prior renders

## Execution Modes

Declare exactly one mode:

### `full`

Use when:

- the brief is sufficiently specified
- design inputs are present or can be completed
- a usable CAD path exists

Expected stop point:

- reference cases
- component selection assumptions
- design pack
- review report
- CAD iteration inputs
- parametric draft model
- CAD iteration report

### `spec-only`

Use when:

- the brief is sufficiently specified
- concept and spec work can continue
- no usable CAD path exists

Expected stop point:

- reference cases
- component selection assumptions
- design pack
- review report
- handoff brief

### `handoff`

Use when:

- the environment lacks critical capabilities
- the inputs are too incomplete to continue safely
- the user primarily needs a downstream package for another collaborator

Expected stop point:

- normalized brief
- assumptions
- handoff brief
- open questions

## Reporting Format

Report the check in this order:

1. capabilities present
2. capabilities missing
3. selected execution mode
4. next artifact to produce

Do not switch modes silently later in the workflow.
