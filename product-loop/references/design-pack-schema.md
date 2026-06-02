# Design Pack Schema

Use `Design Pack` as the machine-readable contract between concept work and downstream modeling.

## Version 1 Fields

### `product_goal`

String. One paragraph maximum. State the product job and outcome.

### `execution_mode`

String enum:

- `full`
- `spec-only`
- `handoff`

### `hard_constraints`

List. Use short objects when possible:

```json
{
  "id": "hc-01",
  "category": "envelope",
  "rule": "Keep the main body within 140 x 38 x 20 mm.",
  "priority": "must"
}
```

### `component_envelopes`

List of component keep-outs or assumed package sizes:

```json
{
  "name": "status display",
  "size_mm": [28, 18, 4],
  "placement_note": "Front-left visual zone"
}
```

### `reference_cases`

List of comparable products, applications, or teardown references used before industrial design:

```json
{
  "case": "mechanical sliding parking number plate",
  "lesson": "A passive slider can hide digits without requiring electronics.",
  "design_implication": "Reserve a shallow front track and finger tab clearance.",
  "source_note": "Comparable product category; verify current suppliers when online research is available."
}
```

### `component_requirements`

List of critical modules and what each one must solve:

```json
{
  "module": "privacy mechanism",
  "requirement": "Hide or reveal the phone number quickly while parked.",
  "envelope_target_mm": [100, 18, 5],
  "design_implication": "The front face needs a track, cover, or rotating element."
}
```

### `component_candidates`

List of candidate parts, modules, or structural material options. Use this for pre-design selection, not final procurement:

```json
{
  "module": "display",
  "candidate": "segmented printed digit cards",
  "approx_envelope_mm": [92, 18, 2],
  "interface_or_mounting": "Mechanical insert behind a clear or open front window",
  "visible_design_impact": "Thin passive body with a precise number window",
  "risk": "Card thickness and retention method vary by supplier"
}
```

### `selected_components`

List of provisional component or module selections that downstream design should treat as assumptions:

```json
{
  "module": "mounting",
  "selection": "silicone anti-slip base plus embedded steel ballast",
  "why": "Keeps the product passive and dashboard-safe.",
  "fixed_constraints": "Requires a broad bottom contact area and heat-resistant pad.",
  "unverified": "Exact pad durometer and adhesive creep in cabin heat",
  "fallback_envelope_mm": [120, 38, 6]
}
```

### `packaging_constraints`

List of spatial rules created by component selection:

- thickness drivers
- visible windows, tracks, buttons, ports, or covers
- battery, magnet, adhesive, hinge, or service keep-outs
- sunlight, heat, abrasion, impact, or sealing constraints

### `sourcing_risks`

List of supply or validation risks that can change the design:

- exact size varies by supplier
- current price or stock was not verified
- module may be too thick for the target form
- battery, magnet, adhesive, display, or material may fail environmental requirements
- research access was unavailable

### `layout_zones`

List of spatial zones. Use explicit intent:

```json
{
  "name": "camera island",
  "surface": "front",
  "purpose": "primary sensor alignment",
  "priority": "must"
}
```

### `mounting_strategy`

Object. Capture how the product sits, hangs, clips, mounts, or docks.

Suggested fields:

- `type`
- `contact_points`
- `support_logic`
- `service_access_notes`

### `style_features`

List of visual features that should survive translation into CAD.

Include:

- silhouette
- feature hierarchy
- surface logic
- CMF cues
- symmetry or asymmetry rules

### `manufacturing_risks`

List of build risks. Keep them concrete:

- service-window crowding
- support arm thickness
- camera alignment sensitivity
- port overhang or insertion conflict

### `forbidden_features`

List of visual or structural moves to avoid.

Examples:

- fake vents with no purpose
- unstable floating forms
- hidden service ports that require disassembly
- decorative asymmetry that breaks layout clarity

### `acceptance_checks`

List of checks used for review and CAD iteration. Prefer structured objects:

```json
{
  "id": "ac-01",
  "title": "Main body envelope",
  "method": "Measure bounding box",
  "pass_condition": "At or below 140 x 38 x 20 mm",
  "priority": "must"
}
```

## Rules

- Keep keys stable across iterations.
- Prefer explicit objects over loose prose in lists.
- Use millimeters for dimensional notes.
- Treat image outputs as references, not as schema fields.
- Add assumptions only when they affect downstream geometry or review.
