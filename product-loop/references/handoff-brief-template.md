# Handoff Brief Template

Use this template when the session cannot continue into CAD, or when the user wants a downstream modeler to take over.

## Required Sections

1. `Modeling target`
   - what should be modeled first
   - what level of fidelity is expected

2. `Execution mode`
   - `spec-only` or `handoff`

3. `Critical envelope`
   - overall size target
   - dimensional hard stops

4. `Suggested part split`
   - main shell
   - covers
   - support or mounting parts
   - interface parts

5. `Priority constraints`
   - must preserve
   - can relax

6. `Selected or assumed components`
   - provisional component path
   - candidate modules or materials
   - fallback envelope if exact parts change

7. `Packaging constraints`
   - thickness drivers
   - keep-outs, windows, tracks, clips, magnets, pads, ports, batteries, or service access
   - heat, UV, vibration, abrasion, sealing, or durability constraints

8. `Component and service assumptions`
   - board access
   - ports
   - buttons
   - sensor alignment
   - component sourcing and packaging feasibility

9. `Sourcing risks`
   - unverified suppliers, dimensions, price, stock, durability, or regional availability

10. `Open questions`
   - unresolved dimensions
   - unresolved mounting details
   - unresolved manufacturability issues

## Output Rule

Write the handoff so that another engineer can begin modeling without re-reading the full chat history.
