# Fase 4 — A esteira de curadoria (composição de funções)
# Regras: SEM for/while, SEM alterar os dados recebidos.
# ATENÇÃO: cada aluno tem REGRAS INDIVIDUAIS (veja contexto/CONTEXTO.md). As suas estão nos textos abaixo.
from functools import reduce  # noqa: F401


def pipe(*funcoes):
    """Devolve uma função que passa o valor pela 1ª função, o resultado pela 2ª, e assim por diante.
    pipe(f, g, h)(x) == h(g(f(x)))"""
    raise NotImplementedError


def passo_limpar_pedidos(eventos):
    """Remove os pedidos inválidos.
    Regra individual limiar_medida = **2**: descarte quem tem "medida" menor que 2."""
    raise NotImplementedError


def passo_deduplicar_pedidos(eventos):
    """Remove pedidos repetidos (dicts totalmente iguais), mantendo a PRIMEIRA ocorrência e a ordem original."""
    raise NotImplementedError


def passo_ranquear_clientes(n):
    """Devolve uma função f(eventos) -> lista dos `n` clientes mais engajados, no formato [[id_usuario, pontos], ...].
    Regra individual criterio_ranking = **frequencia**:
      medida     -> pontos = soma da "medida"
      frequencia -> pontos = QUANTIDADE de pedidos (cada registro vale 1)
    Ordem: mais pontos primeiro; empate: menor id primeiro."""
    raise NotImplementedError


def montar_esteira_pedidos(n):
    """Devolve a esteira completa: limpar -> deduplicar -> ranquear(n), montada com pipe."""
    raise NotImplementedError
