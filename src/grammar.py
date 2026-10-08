"""Grammar and LL(1) predictive parsing table."""

PRODUCTION_TABLE = {
    "FORMULA": {
        "true": ["CONSTANTE"],
        "false": ["CONSTANTE"],
        "prop": ["PROPOSICAO"],
        "(": ["ABREPAREN", "FORMULAINDEFINIDA", "FECHAPAREN"],
    },
    "CONSTANTE": {
        "true": ["true"],
        "false": ["false"],
    },
    "PROPOSICAO": {
        "prop": ["prop"],
    },
    "FORMULAINDEFINIDA": {
        r"\neg": ["OPERATORUNARIO", "FORMULA"],
        r"\wedge": ["OPERATORBINARIO", "FORMULA", "FORMULA"],
        r"\vee": ["OPERATORBINARIO", "FORMULA", "FORMULA"],
        r"\rightarrow": ["OPERATORBINARIO", "FORMULA", "FORMULA"],
        r"\leftrightarrow": ["OPERATORBINARIO", "FORMULA", "FORMULA"],
    },
    "ABREPAREN": {"(": ["("]},
    "FECHAPAREN": {")": [")"]},
    "OPERATORUNARIO": {r"\neg": [r"\neg"]},
    "OPERATORBINARIO": {
        r"\wedge": [r"\wedge"],
        r"\vee": [r"\vee"],
        r"\rightarrow": [r"\rightarrow"],
        r"\leftrightarrow": [r"\leftrightarrow"],
    },
}
