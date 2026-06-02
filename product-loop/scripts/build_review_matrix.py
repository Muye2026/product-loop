#!/usr/bin/env python3

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a markdown review matrix from a Product Loop design pack."
    )
    parser.add_argument("input", type=Path, help="Path to the design-pack JSON file.")
    parser.add_argument(
        "output",
        type=Path,
        nargs="?",
        help="Optional markdown output path. Defaults to stdout when omitted.",
    )
    return parser.parse_args()


def stringify(value):
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)


def normalize_check(item, index):
    if isinstance(item, dict):
        return {
            "id": item.get("id", f"ac-{index:02d}"),
            "title": item.get("title", "Unnamed check"),
            "method": item.get("method", "TBD"),
            "pass_condition": item.get("pass_condition", "TBD"),
            "priority": item.get("priority", "should"),
        }
    return {
        "id": f"ac-{index:02d}",
        "title": stringify(item) or "Unnamed check",
        "method": "TBD",
        "pass_condition": "TBD",
        "priority": "should",
    }


def build_matrix(payload):
    checks = payload.get("acceptance_checks", [])
    lines = [
        "# Review Matrix",
        "",
        f"- Product goal: {payload.get('product_goal', '')}",
        f"- Execution mode: {payload.get('execution_mode', 'spec-only')}",
        "",
        "| ID | Check | Priority | Method | Pass Condition | Status | Notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    if not checks:
        lines.append("| ac-00 | No acceptance checks defined | should | TBD | TBD | TBD | Add checks before review |")
        return "\n".join(lines) + "\n"

    for index, item in enumerate(checks, start=1):
        check = normalize_check(item, index)
        lines.append(
            "| {id} | {title} | {priority} | {method} | {pass_condition} | TBD | |".format(
                **check
            )
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    rendered = build_matrix(payload)

    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
