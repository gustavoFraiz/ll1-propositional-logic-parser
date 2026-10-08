"""Lexical analyzer for the propositional-logic language."""

from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    CONSTANTE = auto()
    PROPOSICAO = auto()
    OPERATORUNARIO = auto()
    OPERATORBINARIO = auto()
    ABREPAREN = auto()
    FECHAPAREN = auto()
    SIMBOLOILEGAL = auto()


@dataclass(frozen=True)
class Token:
    lexeme: str
    token_type: TokenType


UNARY_OPERATORS = {r"\neg"}
BINARY_OPERATORS = {r"\wedge", r"\vee", r"\rightarrow", r"\leftrightarrow"}
CONSTANTS = {"true", "false"}


def tokenize(expression: str) -> list[Token]:
    tokens: list[Token] = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        if char == "(":
            tokens.append(Token(char, TokenType.ABREPAREN))
            i += 1
            continue

        if char == ")":
            tokens.append(Token(char, TokenType.FECHAPAREN))
            i += 1
            continue

        if char == "\\":
            j = i + 1
            while j < len(expression) and expression[j].islower():
                j += 1
            lexeme = expression[i:j]
            if lexeme in UNARY_OPERATORS:
                token_type = TokenType.OPERATORUNARIO
            elif lexeme in BINARY_OPERATORS:
                token_type = TokenType.OPERATORBINARIO
            else:
                token_type = TokenType.SIMBOLOILEGAL
            tokens.append(Token(lexeme, token_type))
            i = j
            continue

        if char.isdigit():
            j = i + 1
            while j < len(expression) and expression[j].isalnum():
                j += 1
            tokens.append(Token(expression[i:j], TokenType.PROPOSICAO))
            i = j
            continue

        if char.islower():
            j = i + 1
            while j < len(expression) and expression[j].islower():
                j += 1
            lexeme = expression[i:j]
            token_type = TokenType.CONSTANTE if lexeme in CONSTANTS else TokenType.SIMBOLOILEGAL
            tokens.append(Token(lexeme, token_type))
            i = j
            continue

        tokens.append(Token(char, TokenType.SIMBOLOILEGAL))
        i += 1

    return tokens
