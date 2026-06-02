# product-loop Validation Results

Date: 2026-06-02

## Global install

- Global install path: `${CODEX_HOME:-$HOME/.codex}/skills/product-loop`
- Install type: symlink
- Symlink target: local checkout `product-loop/` skill package
- Verification: `SKILL.md` is readable through the global path, and the install boundary points only to the inner skill package.

## Helper script smoke test

Input example:
- `examples/desktop-device-demo/design-pack.json`

Results:
- `normalize_design_pack.py`: pass
- `build_review_matrix.py`: pass
- `emit_handoff_brief.py`: pass

Generated artifacts:
- `/tmp/product-loop-design-pack.normalized.json`
- `/tmp/product-loop-review-matrix.md`
- `/tmp/product-loop-handoff-brief.md`

## Behavioral validation matrix

| Test name | Expected mode | Actual mode | Required outputs | Boundary behavior | Result | Notes |
|---|---|---|---|---|---|---|
| spec-only baseline | `spec-only` | `spec-only` | Present: Concept Directions, Appearance Spec, Structure Spec, Design Pack, Review Report, Handoff Brief | Correctly stopped before CAD | Pass | Local output folder recorded outside the public repo |
| midstream resume | `spec-only` | `spec-only` | Present: Appearance Spec, Structure Spec, Design Pack, Review Report | Correctly skipped unnecessary direction exploration | Pass | Local output folder recorded outside the public repo |
| handoff incomplete-input test | `handoff` | `handoff` | Present: Normalized Brief, Assumptions, Open Questions, Handoff Brief | Correctly stopped at handoff boundary | Pass | Local output folder recorded outside the public repo |
| scope boundary test | `handoff` | `handoff` | Present: bounded concept/spec/handoff pack | Correctly refused to imply large-furniture production release | Pass | Local output artifact recorded outside the public repo |
| full-mode decision test | `full` when CAD path is truly usable | `full` | Present: Design Pack, CAD Iteration Inputs, Parametric Draft Model, CAD Iteration Report structure, STEP, STL | Correctly stopped at concept-CAD draft boundary, without implying DFM release | Pass | Local output folder recorded outside the public repo |

## Notes from validation

- `spec-only` mode was selected only when image/spec capability existed but no usable CAD path was confirmed.
- `handoff` mode was selected when the brief or environment was too incomplete for downstream modeling.
- The boundary test did not fabricate wardrobe production tooling, tolerance stacks, or release data.
- The `full` test proved a real local CAD loop through an OCP-compatible Python environment with `OCP`, `trimesh`, and `numpy`.
- The `full` run exported both STEP and STL draft artifacts in the local validation output folder.

## Overall status

`product-loop` passes the planned first-round validation for:
- global installation boundary
- helper-script health
- `spec-only` behavior
- resume behavior
- `handoff` behavior
- scope boundary behavior
- `full` mode selection and draft export behavior

Remaining limitation:
- `full` mode is validated through an OCP-based parametric loop, not through a named end-user CAD application such as FreeCAD or Fusion.
