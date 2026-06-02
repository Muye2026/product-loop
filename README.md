# product-loop

`product-loop` is an open skill package for taking a small hardware product from idea to a reusable design pack, with an optional CAD iteration path when the environment supports it.

It is designed for:

- small consumer electronics
- desktop hardware
- lightweight robotic accessories
- concept-to-spec workflows that need structured handoff artifacts
- industrial design workflows that need component and packaging assumptions before styling

It is not designed for:

- production DFM
- tooling and mold design
- tolerance-stack engineering
- large mechanical systems
- direct final-CAD generation from a single render

## Core idea

The skill enforces three operating rules:

1. Check the environment first.
2. Research comparable products and plausible modules before styling.
3. Use a `Design Pack` as the shared interface between concept work and downstream modeling.
4. Keep repository boundaries clean: installable skill, references, scripts, examples, and repo docs are separated from day one.

## Repository layout

```text
product-loop/
├── README.md
├── 说明.md
├── LICENSE
├── .gitignore
├── product-loop/
│   ├── SKILL.md
│   ├── agents/
│   ├── references/
│   └── scripts/
├── examples/
│   └── desktop-device-demo/
└── assets/
    └── diagrams/
```

The installable skill lives in [`product-loop/`](./product-loop). The `examples/` directory is documentation-only and should not be merged into the skill folder when you install it.

## What the skill does

The workflow is split into six main phases, with one optional architecture gate and one required component-selection pass:

1. `Phase 0: Environment Check`
2. `Phase 1: Brief Clarification`
3. `Phase 1.5: Module Architecture Framing` when unresolved module choices would materially change the product
4. `Phase 1.6: Research-backed Component Selection`
5. `Phase 2: Direction Exploration`
6. `Phase 3: Visual Convergence`
7. `Phase 4: Design Translation`
8. `Phase 5: CAD Loop or Handoff`

The environment check selects one execution mode:

- `full`: CAD-capable environment; continue into a parametric draft-model loop
- `spec-only`: no CAD environment; stop at a design pack plus review artifacts
- `handoff`: environment or inputs are incomplete; emit a downstream handoff package

## Standard outputs

Complete `spec-only` and `full` runs should produce:

- `Reference Cases`
- `Candidate Components`
- `Selected or Assumed Components`
- `Packaging Constraints`
- `Concept Directions`
- `Render Set`
- `Appearance Spec`
- `Structure Spec`
- `Design Pack`
- `Review Report`

`handoff` mode may stop earlier when inputs or environment capability are incomplete. In that case, the expected outputs are:

- `Normalized Brief`
- `Assumptions`
- `Open Questions`
- `Handoff Brief`

`full` mode adds:

- `CAD Iteration Inputs`
- `Parametric Draft Model`
- `CAD Iteration Report`

## Design Pack contract

Version 1 of the structured `Design Pack` uses these top-level fields:

- `product_goal`
- `execution_mode`
- `hard_constraints`
- `component_envelopes`
- `reference_cases`
- `component_requirements`
- `component_candidates`
- `selected_components`
- `packaging_constraints`
- `sourcing_risks`
- `layout_zones`
- `mounting_strategy`
- `style_features`
- `manufacturing_risks`
- `forbidden_features`
- `acceptance_checks`

The skill ships helper scripts that normalize the design pack, generate a review matrix, and emit a handoff brief.

## Install

Copy or symlink the inner `product-loop/` directory into your Codex skills directory.

Example:

```bash
cp -R product-loop/product-loop "${CODEX_HOME:-$HOME/.codex}/skills/"
```

After installation, Codex should discover the skill as `$product-loop`.

## Example

See [`examples/desktop-device-demo/`](./examples/desktop-device-demo/) for a complete non-private example that includes:

- a normalized brief
- concept directions
- appearance and structure specs
- a structured design pack
- a review report

See [`examples/parking-number-plate-demo/`](./examples/parking-number-plate-demo/) for a component-selection-focused example that shows reference cases, candidate modules, provisional selections, and packaging constraints before concept directions.

## Helper scripts

The skill includes three lightweight Python helpers:

- [`normalize_design_pack.py`](./product-loop/scripts/normalize_design_pack.py)
- [`build_review_matrix.py`](./product-loop/scripts/build_review_matrix.py)
- [`emit_handoff_brief.py`](./product-loop/scripts/emit_handoff_brief.py)

Example usage:

```bash
python3 product-loop/scripts/normalize_design_pack.py \
  examples/desktop-device-demo/design-pack.json \
  /tmp/design-pack.normalized.json

python3 product-loop/scripts/build_review_matrix.py \
  examples/desktop-device-demo/design-pack.json \
  /tmp/review-matrix.md

python3 product-loop/scripts/emit_handoff_brief.py \
  examples/desktop-device-demo/design-pack.json \
  /tmp/handoff-brief.md
```

## Notes for maintainers

- Keep the skill body concise; push detailed templates and schemas into `references/`.
- Do not bake local machine paths, proprietary repositories, or personal CAD setups into the skill.
- Treat the example as a public demo artifact, not as product-specific source truth.
