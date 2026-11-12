# Fase 4 — A esteira de curadoria (composição de funções)
# Regras: SEM for/while, SEM alterar os dados recebidos.
from functools import reduce

LIMIAR_MEDIDA = 2  # regra individual: pedidos com medida < 2 são descartados
CRITERIO_RANKING = "frequencia"  # regra individual: cada pedido vale 1 ponto


def pipe(*funcoes):
    """Devolve uma função que passa o valor pela 1ª função, o resultado pela 2ª, e assim por diante.
    pipe(f, g, h)(x) == h(g(f(x)))"""
    return lambda valor: reduce(lambda acc, f: f(acc), funcoes, valor)


def passo_limpar_pedidos(eventos):
    """Remove os pedidos inválidos.
    Regra individual limiar_medida = **2**: descarte quem tem "medida" menor que 2."""
    return [e for e in eventos if e["medida"] >= LIMIAR_MEDIDA]


def passo_deduplicar_pedidos(eventos):
    """Remove pedidos repetidos (dicts totalmente iguais), mantendo a PRIMEIRA ocorrência e a ordem original."""
    return reduce(lambda vistos, e: vistos if e in vistos else vistos + [e], eventos, [])


def passo_ranquear_clientes(n):
    """Devolve uma função f(eventos) -> lista dos `n` clientes mais engajados, no formato [[id_usuario, pontos], ...].
    Regra individual criterio_ranking = **frequencia**:
      medida     -> pontos = soma da "medida"
      frequencia -> pontos = QUANTIDADE de pedidos (cada registro vale 1)
    Ordem: mais pontos primeiro; empate: menor id primeiro."""
    peso = (lambda e: 1) if CRITERIO_RANKING == "frequencia" else (lambda e: e["medida"])

    def ranquear(eventos):
        pontos = reduce(lambda acc, e: {**acc, e["usuario"]: acc.get(e["usuario"], 0) + peso(e)}, eventos, {})
        return [[u, p] for u, p in sorted(pontos.items(), key=lambda par: (-par[1], par[0]))][:n]

    return ranquear


def montar_esteira_pedidos(n):
    """Devolve a esteira completa: limpar -> deduplicar -> ranquear(n), montada com pipe."""
    return pipe(passo_limpar_pedidos, passo_deduplicar_pedidos, passo_ranquear_clientes(n))
