# 🍕 Fase 3 — A fábrica de regras

> **Missão:** criar funções que **fabricam outras funções** para as regras de negócio da BitFood.
> **Recompensa:** 15 XP · distintivo 🏭 *Fábrica de funções*

## O que você vai aprender

- Funções são **valores**: podem ser guardadas, passadas e devolvidas.
- O que é uma **closure** (a função "lembra" os valores com que foi criada).
- Parametrizar regras sem copiar e colar código.

## Vamos entender

Pense em uma **forma de biscoito**. A forma (a função fábrica) é configurada uma vez — estrela, coração — e depois produz quantos biscoitos você quiser. Já a função `criar_desconto(20)` devolve uma função "desconto de 20%": você a cria uma vez e usa em todos os preços.

O valor `20` fica "preso" dentro da função devolvida. Isso é uma **closure**.

## Faça como eu fiz

Crie `treino/regras.py`:

```python
def criar_taxa(percentual):
    return lambda preco: preco + preco * percentual // 100

taxa10 = criar_taxa(10)
taxa50 = criar_taxa(50)
print(taxa10(1000), taxa50(1000))   # 1100 1500: cada função lembra o seu percentual
```

## Mão na massa

Abra `src/fase3.py` e implemente as 4 fábricas da **BitFood**:

| Função | Devolve uma função que... |
|---|---|
| `criar_filtro_culinaria(categoria)` | diz se um prato pertence à categoria recebida (culinária) |
| `criar_restricao_classificacao_prato(limite)` | diz se a classificação do prato é no máximo `limite` |
| `criar_desconto_prato(percentual)` | calcula o preço com desconto (inteiro, em centavos) |
| `criar_promo_aniversario_cliente(mes, percentual)` | aplica o desconto só se o cliente faz aniversário naquele mês |

Os testes usam os **seus** parâmetros (veja `contexto/CONTEXTO.md`): categoria em foco **Brasileira**, desconto de **10%**, mês **7**, classificação limite **12**.

As suas **regras individuais** desta fase: arredondamento do desconto **cima**, restrição **ate** e promoção no **mes_do_aniversario**. Elas ficam escritas dentro das suas funções. Reaproveite `criar_desconto_prato` dentro de `criar_promo_aniversario_cliente`: uma fábrica pode usar outra.

Registre no `JUSTIFICATIVA.md`: o que cada função "lembra" depois de criada.

## Rodar os testes

`python placar.py`

## Para saber mais

- A técnica de transformar uma função de 2 argumentos em duas funções de 1 argumento se chama **currying**.
- Em Python, também é possível usar `functools.partial` para fixar argumentos.

## O que aprendemos

- Funções de primeira classe podem ser devolvidas por outras funções.
- Closure = função que carrega consigo os valores do contexto em que nasceu.
- Fábricas evitam código repetido e deixam as regras configuráveis.
