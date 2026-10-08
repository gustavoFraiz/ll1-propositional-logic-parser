# Grammar and predictive parsing

## Production rules

| # | Production |
|---:|---|
| 1 | `FORMULA -> CONSTANTE` |
| 2 | `FORMULA -> PROPOSICAO` |
| 3 | `FORMULA -> ABREPAREN FORMULAINDEFINIDA FECHAPAREN` |
| 4 | `CONSTANTE -> true` |
| 5 | `CONSTANTE -> false` |
| 6 | `PROPOSICAO -> [0-9][0-9a-z]*` |
| 7 | `FORMULAINDEFINIDA -> OPERATORUNARIO FORMULA` |
| 8 | `FORMULAINDEFINIDA -> OPERATORBINARIO FORMULA FORMULA` |
| 9 | `ABREPAREN -> (` |
| 10 | `FECHAPAREN -> )` |
| 11 | `OPERATORUNARIO -> \neg` |
| 12 | `OPERATORBINARIO -> \wedge` |
| 13 | `OPERATORBINARIO -> \vee` |
| 14 | `OPERATORBINARIO -> \rightarrow` |
| 15 | `OPERATORBINARIO -> \leftrightarrow` |

## FIRST sets

```text
FIRST(FORMULA) = { true, false, prop, ( }
FIRST(CONSTANTE) = { true, false }
FIRST(PROPOSICAO) = { prop }
FIRST(FORMULAINDEFINIDA) = { \neg, \wedge, \vee, \rightarrow, \leftrightarrow }
FIRST(ABREPAREN) = { ( }
FIRST(FECHAPAREN) = { ) }
FIRST(OPERATORUNARIO) = { \neg }
FIRST(OPERATORBINARIO) = { \wedge, \vee, \rightarrow, \leftrightarrow }
```

## Predictive table

| Non-terminal | `true` | `false` | `prop` | `(` | `)` | `\neg` | `\wedge` | `\vee` | `\rightarrow` | `\leftrightarrow` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| FORMULA | 1 | 1 | 2 | 3 |  |  |  |  |  |  |
| CONSTANTE | 4 | 5 |  |  |  |  |  |  |  |  |
| PROPOSICAO |  |  | 6 |  |  |  |  |  |  |  |
| FORMULAINDEFINIDA |  |  |  |  |  | 7 | 8 | 8 | 8 | 8 |
| ABREPAREN |  |  |  | 9 |  |  |  |  |  |  |
| FECHAPAREN |  |  |  |  | 10 |  |  |  |  |  |
| OPERATORUNARIO |  |  |  |  |  | 11 |  |  |  |  |
| OPERATORBINARIO |  |  |  |  |  |  | 12 | 13 | 14 | 15 |

The table used by the cleaned implementation is encoded in `src/grammar.py`.
