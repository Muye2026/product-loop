# Component Selection

## Reference Cases

1. Passive sliding parking number plate
   - Module strategy: printed or inserted digits behind a sliding privacy cover.
   - Lesson: keeps the product thin and avoids battery safety concerns.
   - Design implication: reserve a front track, slider tab clearance, and number-window tolerance.
   - Source note: common marketplace product category; verify current suppliers during a live run.

2. Flip-cover parking number plate
   - Module strategy: hinged or rotating cover hides the digits.
   - Lesson: privacy action is obvious, but hinge thickness can dominate side profile.
   - Design implication: side elevation must account for hinge barrel or pivot pins.
   - Source note: comparable commercial mechanism pattern.

3. LED or backlit parking number display
   - Module strategy: active light source, battery, switch, and diffuser.
   - Lesson: improves night visibility but increases thickness, service access, heat risk, and cost.
   - Design implication: needs a service panel, power story, and thermal/material caution.
   - Source note: use only if illumination is a hard requirement.

4. Magnetic or silicone dashboard base
   - Module strategy: soft pad, embedded metal weight, magnet, or gel base.
   - Lesson: stable placement matters more than decorative form.
   - Design implication: bottom footprint and material transition should be designed, not hidden.
   - Source note: verify magnet/metal placement against vehicle safety and heat concerns.

## Component Requirements

- Number display: show 11-12 digits at windshield viewing distance; keep digit area around 92 x 18 mm.
- Privacy mechanism: cover digits in one motion; fit within a shallow front or top track.
- Mounting base: resist dashboard slip without permanent adhesive; tolerate heat and UV exposure.
- Shell material: protect the digit insert and mechanism while staying visually calm.
- Optional visibility aid: reflective or photoluminescent digits without adding an electronics stack.

## Candidate Components

- Display candidate A: segmented printed digit cards
  - Approximate envelope: 92 x 18 x 2 mm.
  - Mounting: retained in a front window or shallow tray.
  - Design impact: thin, passive, easy to make visually precise.
  - Risk: supplier card thickness and character spacing vary.

- Display candidate B: magnetic number tiles
  - Approximate envelope: 95 x 20 x 4 mm including retention layer.
  - Mounting: magnets or steel-backed tiles in a tray.
  - Design impact: easier number changes, but thicker front module.
  - Risk: small parts, retention reliability, and heat behavior need validation.

- Privacy candidate A: sliding cover
  - Approximate envelope: 105 x 22 x 3 mm.
  - Mounting: top or front track with stop features.
  - Design impact: long clean horizontal gesture, minimal side thickness.
  - Risk: track friction, dust, and rattle.

- Privacy candidate B: flip cover
  - Approximate envelope: 105 x 24 x 5 mm at hinge side.
  - Mounting: side pins or living hinge.
  - Design impact: more explicit privacy action, but visually bulkier.
  - Risk: hinge durability and dashboard clearance.

- Base candidate A: silicone anti-slip pad plus weighted internal plate
  - Approximate envelope: 120 x 36 x 5 mm.
  - Mounting: bottom pad bonded or mechanically captured by shell.
  - Design impact: broad stable stance and soft underside detail.
  - Risk: pad durometer and heat aging are unverified.

- Base candidate B: magnetic base plus steel insert
  - Approximate envelope: 110 x 30 x 5 mm.
  - Mounting: embedded magnets and metal plate.
  - Design impact: compact base, but must hide magnet pattern.
  - Risk: dashboard compatibility and heat/adhesive concerns.

## Selected or Assumed Components

- Display: segmented printed digit cards
  - Why: lowest thickness and no electronics.
  - Fixed constraints: 92 x 18 mm number window, front tray retention, clear digit spacing.
  - Unverified: exact card supplier thickness and print durability.
  - Fallback envelope: 98 x 22 x 4 mm.

- Privacy: sliding cover
  - Why: thin one-hand privacy action with controlled horizontal product language.
  - Fixed constraints: shallow track, slider stop, visible tab, anti-rattle detail.
  - Unverified: friction and rattle after heat exposure.
  - Fallback envelope: 110 x 24 x 5 mm.

- Base: silicone anti-slip pad plus weighted internal plate
  - Why: dashboard-safe and passive without exposed permanent adhesive.
  - Fixed constraints: broad bottom footprint, captured pad edge, internal ballast zone.
  - Unverified: pad durometer and heat aging.
  - Fallback envelope: 125 x 40 x 7 mm.

## Packaging Constraints

- Target body thickness should stay near 12-14 mm after number cards, slider, shell, and base are stacked.
- Front number window should be about 92 x 18 mm, with a small reveal margin.
- Slider track needs end stops, finger tab clearance, and anti-rattle features.
- Base must include a soft pad and a stable contact footprint; do not let styling reduce bottom area.
- Avoid electronics unless illumination becomes a hard requirement.

## Sourcing Risks

- Digit card dimensions vary by supplier.
- Silicone pad performance under parked-car heat is unverified.
- Magnetic bases may not suit every dashboard and can create misleading stability assumptions.
- Current availability, price, and exact supplier dimensions were not verified in this static example.
