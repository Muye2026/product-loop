#!/usr/bin/env python3

import argparse
import json
from collections import OrderedDict
from pathlib import Path


DEFAULTS = OrderedDict(
    [
        ("product_goal", ""),
        ("execution_mode", "spec-only"),
        ("hard_constraints", []),
        ("component_envelopes", []),
        ("reference_cases", []),
        ("component_requirements", []),
        ("component_candidates", []),
        ("selected_components", []),
        ("packaging_constraints", []),
        ("sourcing_risks", []),
        ("layout_zones", []),
        ("mounting_strategy", {}),
        ("style_features", []),
        ("manufacturing_risks", []),
        ("forbidden_features", []),
        ("acceptance_checks", []),
    ]
)

VALID_MODES = {"full", "spec-only", "handoff"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize a Product Loop design-pack JSON document."
    )
    parser.add_argument("input", type=Path, help="Path to the source design-pack JSON file.")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Optional output path. Defaults to stdout when omitted.",
    )
    return parser.parse_args()


def coerce_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def coerce_dict(value):
    if value is None:
        return {}
    if isinstance(value, dict):
        return value
    return {"value": value}


def normalize(data):
    normalized = OrderedDict()
    source = dict(data or {})

    for key, default in DEFAULTS.items():
        value = source.pop(key, default)
        if key in {
            "hard_constraints",
            "component_envelopes",
            "reference_cases",
            "component_requirements",
            "component_candidates",
            "selected_components",
            "packaging_constraints",
            "sourcing_risks",
            "layout_zones",
            "style_features",
            "manufacturing_risks",
            "forbidden_features",
            "acceptance_checks",
        }:
            value = coerce_list(value)
        elif key == "mounting_strategy":
            value = coerce_dict(value)
        elif key == "execution_mode":
            if value not in VALID_MODES:
                value = "spec-only"
        elif value is None:
            value = default
        normalized[key] = value

    for key in sorted(source):
        normalized[key] = source[key]

    return normalized


def main() -> int:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    normalized = normalize(payload)
    rendered = json.dumps(normalized, ensure_ascii=True, indent=2) + "\n"

    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
