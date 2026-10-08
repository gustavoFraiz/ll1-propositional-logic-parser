"""Predictive LL(1) parser."""

from .grammar import PRODUCTION_TABLE
from .lexer import Token, TokenType


TERMINALS = {
    "true", "false", "prop", "(", ")",
    r"\neg", r"\wedge", r"\vee", r"\rightarrow", r"\leftrightarrow", "$",
}


def token_to_terminal(token: Token) -> str:
    if token.token_type == TokenType.PROPOSICAO:
        return "prop"
    return token.lexeme


def parse(tokens: list[Token]) -> bool:
    if any(token.token_type == TokenType.SIMBOLOILEGAL for token in tokens):
        return False

    stack = ["$", "FORMULA"]
    buffer = [token_to_terminal(token) for token in tokens] + ["$"]
    cursor = 0

    while stack:
        top = stack.pop()
        lookahead = buffer[cursor]

        if top in TERMINALS:
            if top != lookahead:
                return False
            cursor += 1
            continue

        production = PRODUCTION_TABLE.get(top, {}).get(lookahead)
        if production is None:
            return False
        stack.extend(reversed(production))

    return cursor == len(buffer)
