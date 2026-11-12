# 🍕 Fase 4 — A esteira de curadoria

> **Missão:** montar uma **linha de montagem** que limpa, deduplica e ranqueia os pedidos da BitFood.
> **Recompensa:** 15 XP · distintivo 🚚 *Mestre da esteira*

## O que você vai aprender

- Composição de funções: ligar a saída de uma na entrada da próxima.
- Construir o seu próprio `pipe`.
- Pensar em **fluxo de dados** em vez de passos soltos.

## Vamos entender

Em uma **linha de montagem de fábrica**, cada estação faz uma coisa e passa a peça adiante. Ninguém precisa saber o que as outras fazem. Com funções puras é igual: cada uma recebe um valor e devolve um novo, e a composição `pipe(f, g, h)` os encadeia: `h(g(f(x)))`.

Funciona *porque* as funções são puras: nenhuma estraga o que a outra precisa.

## Faça como eu fiz

Crie `treino/esteira.py`:

```python
from functools import reduce

def pipe(*funcoes):
    return lambda valor: reduce(lambda acc, f: f(acc), funcoes, valor)

limpar = lambda s: s.strip()
maiuscula = lambda s: s.upper()
exclamar = lambda s: s + "!"

saudar = pipe(limpar, maiuscula, exclamar)
print(saudar("  olá mundo  "))   # OLÁ MUNDO!
```

Note que `pipe` é só um `reduce` em que o acumulador é o **valor** e cada item é uma **função**.

## Mão na massa

Abra `src/fase4.py`. Os dados de trabalho são `eventos_brutos`: eles têm registros **repetidos** e **inválidos** (medida 0).

| Função | O que faz |
|---|---|
| `pipe` | encadeia funções, da esquerda para a direita |
| `passo_limpar_pedidos` | remove pedidos com medida **menor que 2** (regra individual) |
| `passo_deduplicar_pedidos` | remove repetidos, mantendo a primeira ocorrência |
| `passo_ranquear_clientes(n)` | devolve os `n` clientes mais engajados `[[id, pontos], ...]`, com critério **frequencia** (regra individual) |
| `montar_esteira_pedidos(n)` | junta tudo com `pipe` (no seu caso, `n = 5`) |

Registre no `JUSTIFICATIVA.md`: o que muda no resultado se você trocar a ordem das etapas (por exemplo, ranquear antes de limpar)?

## Rodar os testes

`python placar.py`

## Para saber mais

- Composição é o mesmo princípio dos *pipes* do terminal (`cat arquivo | sort | uniq`).
- Bibliotecas funcionais trazem `compose` (da direita para a esquerda) e `pipe` (da esquerda para a direita).

## O que aprendemos

- Composição liga funções pequenas em fluxos maiores.
- `pipe` pode ser escrito com `reduce`.
- Funções puras são fáceis de combinar porque não têm efeitos escondidos.
