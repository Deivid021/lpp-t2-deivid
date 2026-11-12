# 🍕 Fase 1 — A caça às funções impuras

> **Missão:** encontrar o que está contaminando o código herdado da BitFood e transformar cada função em uma **função pura**.
> **Recompensa:** 10 XP · distintivo 🧼 *Puro de coração*

## O que você vai aprender

- O que é uma função pura e o que são efeitos colaterais.
- Por que alterar a entrada ou usar variável global causa bugs difíceis de reproduzir.
- Como devolver dados **novos** em vez de alterar os existentes (imutabilidade).

## Vamos entender

Pense numa **máquina de café**. Uma máquina *pura* sempre entrega o mesmo café para o mesmo pedido e não mexe em mais nada na cozinha. Uma máquina *impura* muda o estoque de açúcar sem avisar, e o café de hoje depende do que aconteceu ontem.

Uma função é **pura** quando:

1. a mesma entrada **sempre** produz a mesma saída;
2. ela **não altera** nada fora dela (nem os argumentos recebidos, nem variáveis globais, nem arquivos).

Quando uma função altera algo fora dela, dizemos que tem **efeito colateral**. Em um relatório, isso significa que rodar duas vezes pode dar resultados diferentes.

## Faça como eu fiz

Crie `treino/cafe.py` e execute os dois exemplos, observando a diferença:

```python
pedido = {"cafe": "latte", "preco": 1000}

def aplicar_taxa_impura(p):
    p["preco"] += 100        # altera o pedido que veio de fora!
    return p

def aplicar_taxa_pura(p):
    return {**p, "preco": p["preco"] + 100}   # devolve um pedido NOVO

print(aplicar_taxa_pura(pedido), pedido)     # pedido continua com 1000
print(aplicar_taxa_impura(pedido), pedido)   # pedido virou 1100 — efeito colateral
```

Truques para não alterar: `{**d, "campo": novo}` cria um dict novo; `[*lista, x]` cria uma lista nova; `sorted(lista)` devolve uma lista ordenada nova (já `lista.sort()` altera a original).

## Mão na massa

Abra `src/fase1.py`. As 4 funções da **BitFood** estão contaminadas. Reescreva cada uma:

| Função | O que deve fazer |
|---|---|
| `padronizar_nomes_clientes` | devolver lista nova de clientes com o nome em **maiusculas** |
| `registrar_pedido` | devolver um novo registro de pedido com a "medida" (unidades pedidas) aumentada |
| `proximo_codigo_pedido` | devolver `ultimo + 2`, sem estado escondido |
| `ordenar_pratos_por_preco` | devolver lista nova de pratos ordenada por preço **decrescente** (empate: menor id) |

As palavras em negrito são as **suas regras individuais** (tabela completa em `contexto/CONTEXTO.md`).

Os testes entregam dados **congelados**: se a sua função tentar alterá-los, ela falha. Anote no `JUSTIFICATIVA.md` qual era o efeito colateral de cada função e como você o removeu.

## Rodar os testes

`python placar.py`

## Para saber mais

- Funções puras são fáceis de testar: não precisam de preparação nem de limpeza.
- Pureza não proíbe criar variáveis **dentro** da função; proíbe alterar o que está **fora**.

## O que aprendemos

- Função pura = mesma entrada, mesma saída, sem efeitos colaterais.
- Em vez de alterar, devolva **dados novos**.
- Estado global escondido torna o resultado imprevisível.
