# Component Selection

Use this reference during `Phase 1.6` to turn a product goal and module architecture into researched, package-aware component assumptions before industrial design.

## Purpose

Prevent appearance work from drifting away from feasible hardware. This phase is not a final engineering BOM. It is a pre-design selection pass that makes the size, openings, materials, mounting, power, and sourcing assumptions concrete enough for industrial design and draft CAD.

## Research Inputs

When research access is available, inspect a balanced mix of:

- comparable commercial products
- teardown, repair, or maker build notes
- marketplace listings for current modules and accessories
- manufacturer pages and distributor references
- structural material and mechanism examples

Use globally balanced sources by default. If a market is specified, prioritize that market and use other regions as cross-checks.

When research access is unavailable, continue with clearly labeled assumptions and record the missing research in `Sourcing Risks`.

## Required Outputs

### `Reference Cases`

Summarize 3-6 comparable products or application cases.

For each case, capture:

- case name or product type
- observed module strategy
- appearance or structure lesson
- component or mechanism clue
- source note or research gap

### `Component Requirements`

List critical modules and what each must solve.

Use short objects or bullets with:

- module name
- functional requirement
- envelope target or limit
- interface or mounting need
- environmental or durability need
- industrial-design implication

### `Candidate Components`

For each critical module, provide 2-4 plausible candidates.

For each candidate, capture:

- candidate name or type
- example part, module, or material category when available
- approximate size or envelope
- interface, mounting, or assembly notes
- visible design impact
- main sourcing, cost, or validation risk

Do not claim exact availability, price, or stock unless verified in the current session.

### `Selected or Assumed Components`

Recommend one provisional component path per critical module.

For each selected or assumed item, state:

- why it was selected
- what design constraints it fixes
- what remains unverified
- fallback envelope if the exact part changes

### `Packaging Constraints`

Translate selected components into spatial rules:

- total product thickness drivers
- display or indicator window size
- ports, buttons, sliders, hinges, clips, magnets, pads, or fasteners
- cable, battery, antenna, or service keep-outs
- thermal, sealing, sunlight, impact, or abrasion constraints

### `Sourcing Risks`

Capture risks that could force redesign:

- candidate part may be unavailable or region-specific
- exact size may vary by supplier
- consumer module may be too thick or too fragile
- display, battery, magnet, adhesive, or material may fail environmental conditions
- no source was checked because research access was unavailable

## Selection Behavior

In `checkpointed` mode, recommend a component set and continue unless:

- no candidate can satisfy a hard constraint
- the selected path changes the product architecture materially
- the user explicitly asks to approve components first

In `auto` mode, select a provisional path, state the reasoning, and continue.

Never hide a hard conflict between component size and desired appearance. If a product cannot fit the selected components, say so before generating directions.

## Parking Number Plate Coverage

For parking-number-plate or temporary vehicle contact-display products, cover at least:

- number display method: printed digits, segmented insert cards, e-ink, LCD, LED, or backlit film
- privacy mechanism: slider, flip cover, rotating drum, magnetic cover, or electronic blanking
- mounting: magnetic base, adhesive gel pad, silicone anti-slip base, clip, suction, or weighted base
- illumination: none, photoluminescent material, reflective print, LED edge light, or backlight
- power: passive, replaceable coin cell, rechargeable lithium cell, solar assist, or vehicle-powered
- sunlight and cabin heat: UV stability, warping risk, adhesive creep, battery safety, and display readability
- materials: ABS, PC, aluminum shell, silicone pad, acrylic light guide, steel plate, or magnet

The industrial-design directions must reflect these choices. For example, a passive magnetic slider can be thin and mechanical; an LED or e-ink path needs a thicker electronics zone, service access, and a battery or charging story.
