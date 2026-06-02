#!/usr/bin/env python3

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit a markdown handoff brief from a Product Loop design pack."
    )
    parser.add_argument("input", type=Path, help="Path to the design-pack JSON file.")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Optional markdown output path. Defaults to stdout when omitted.",
    )
    return parser.parse_args()


def render_list(items, empty_text="None provided."):
    if not items:
        return f"- {empty_text}"
    lines = []
    for item in items:
        if isinstance(item, dict):
            head = (
                item.get("name")
                or item.get("case")
                or item.get("module")
                or item.get("candidate")
                or item.get("selection")
                or item.get("id")
                or item.get("title")
                or "Item"
            )
            detail_parts = []
            for key, value in item.items():
                if key in {"name", "case", "module", "candidate", "selection", "id", "title"}:
                    continue
                detail_parts.append(f"{key}: {value}")
            detail = "; ".join(detail_parts)
            lines.append(f"- {head}" + (f" ({detail})" if detail else ""))
        else:
            lines.append(f"- {item}")
    return "\n".join(lines)


def build_brief(payload):
    mounting = payload.get("mounting_strategy", {})
    lines = [
        "# Handoff Brief",
        "",
        "## Modeling target",
        payload.get("product_goal", "Model a first-pass draft from the approved design direction."),
        "",
        "## Execution mode",
        f"- {payload.get('execution_mode', 'spec-only')}",
        "",
        "## Critical envelope and hard constraints",
        render_list(payload.get("hard_constraints", []), "Add hard constraints before downstream modeling."),
        "",
        "## Suggested part split",
        render_list(
            mounting.get("suggested_part_split", []),
            "Main shell, support structure, and service-facing details should be defined by the next modeler.",
        ),
        "",
        "## Component and service assumptions",
        render_list(payload.get("component_envelopes", []), "No component assumptions recorded."),
        "",
        "## Reference cases",
        render_list(payload.get("reference_cases", []), "No reference cases recorded."),
        "",
        "## Component requirements",
        render_list(payload.get("component_requirements", []), "No component requirements recorded."),
        "",
        "## Candidate components",
        render_list(payload.get("component_candidates", []), "No candidate components recorded."),
        "",
        "## Selected or assumed components",
        render_list(payload.get("selected_components", []), "No selected or assumed components recorded."),
        "",
        "## Packaging constraints",
        render_list(payload.get("packaging_constraints", []), "No packaging constraints recorded."),
        "",
        "## Layout zones",
        render_list(payload.get("layout_zones", []), "No layout zones recorded."),
        "",
        "## Mounting strategy",
    ]

    if mounting:
        for key, value in mounting.items():
            if key == "suggested_part_split":
                continue
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- No mounting strategy recorded.")

    lines.extend(
        [
            "",
            "## Style features to preserve",
            render_list(payload.get("style_features", []), "No style features recorded."),
            "",
            "## Manufacturing risks",
            render_list(payload.get("manufacturing_risks", []), "No manufacturing risks recorded."),
            "",
            "## Sourcing risks",
            render_list(payload.get("sourcing_risks", []), "No sourcing risks recorded."),
            "",
            "## Forbidden features",
            render_list(payload.get("forbidden_features", []), "No forbidden features recorded."),
            "",
            "## Acceptance checks",
            render_list(payload.get("acceptance_checks", []), "No acceptance checks recorded."),
            "",
            "## Open questions",
            "- Confirm unresolved dimensions, stack-up assumptions, and service clearances before detailed CAD.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    rendered = build_brief(payload)

    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
