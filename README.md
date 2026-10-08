# LL(1) Propositional Logic Parser

A lexer and predictive **LL(1) parser implemented from scratch in Python** for a small propositional-logic grammar.

This project was originally developed as an undergraduate compiler/formal-languages assignment and has been reorganized here for archival and portfolio purposes. The repository preserves the original algorithm, grammar and co-authorship while presenting the implementation in a cleaner source layout.

## Authors

- **Gustavo Barbosa**
- **Pedro Gonçalves Classen**

The repository preserves the original co-authorship of the project.

## What it does

The program processes propositional-logic expressions in two stages:

1. **Lexical analysis**
   - recognizes boolean constants;
   - recognizes propositions;
   - recognizes parentheses;
   - recognizes unary and binary logical operators;
   - reports illegal symbols.

2. **LL(1) syntactic analysis**
   - converts proposition tokens to a common `prop` terminal;
   - uses a predictive parsing table;
   - maintains a parsing stack and lookahead buffer;
   - accepts or rejects each expression according to the grammar.

Supported logical operators:

| Operator | Meaning |
| --- | --- |
| `\neg` | NOT |
| `\wedge` | AND |
| `\vee` | OR |
| `\rightarrow` | implication |
| `\leftrightarrow` | biconditional |

## Grammar

```text
FORMULA -> CONSTANTE
FORMULA -> PROPOSICAO
FORMULA -> ABREPAREN FORMULAINDEFINIDA FECHAPAREN

CONSTANTE -> true
CONSTANTE -> false

PROPOSICAO -> [0-9][0-9a-z]*

FORMULAINDEFINIDA -> OPERATORUNARIO FORMULA
FORMULAINDEFINIDA -> OPERATORBINARIO FORMULA FORMULA

ABREPAREN -> (
FECHAPAREN -> )

OPERATORUNARIO -> \neg

OPERATORBINARIO -> \wedge
OPERATORBINARIO -> \vee
OPERATORBINARIO -> \rightarrow
OPERATORBINARIO -> \leftrightarrow
```

More details about the FIRST sets and predictive table are in [`docs/grammar.md`](docs/grammar.md).

## Repository structure

```text
.
├── README.md
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── lexer.py
│   ├── parser.py
│   ├── grammar.py
│   └── main.py
├── tests/
│   ├── test_parser.py
│   └── data/
│       └── sample.txt
└── docs/
    └── grammar.md
```

## Running

Requires Python 3.10+.

```bash
python -m src.main tests/data/sample.txt
```

Input format:

```text
4
true
(\neg false)
(\wedge true false)
(\rightarrow 1abc (\vee true false))
```

The first line contains the number of expressions that follow.

Expected output:

```text
valid
valid
valid
valid
```

## Tests

```bash
python -m unittest discover tests
```

The cleaned implementation was validated locally with **6 passing tests** during the migration.

## Portfolio note

The source under `src/` is a structural cleanup of the recovered notebook implementation: responsibilities were separated into modules and the command-line interface was made local-file friendly. The algorithm and project concept remain attributable to the original authors.

## License

No open-source license has been added. Because this is a co-authored academic project, licensing should be agreed upon by both authors before one is selected.
