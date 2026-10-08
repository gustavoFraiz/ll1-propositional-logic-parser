"""Command-line interface for the LL(1) parser."""

import argparse
from pathlib import Path

from .lexer import tokenize
from .parser import parse


def read_expressions(path: Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError("Input file is empty.")

    try:
        expected_count = int(lines[0].strip())
    except ValueError as exc:
        raise ValueError("The first line must contain the number of expressions.") from exc

    expressions = lines[1:]
    if len(expressions) < expected_count:
        raise ValueError(f"Expected {expected_count} expressions, but found {len(expressions)}.")

    return expressions[:expected_count]


def main() -> None:
    argument_parser = argparse.ArgumentParser(
        description="Validate propositional-logic expressions with an LL(1) parser."
    )
    argument_parser.add_argument("input_file", type=Path)
    args = argument_parser.parse_args()

    for expression in read_expressions(args.input_file):
        valid = parse(tokenize(expression))
        print("valid" if valid else "invalid")


if __name__ == "__main__":
    main()
