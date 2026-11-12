# Fase 1 — A caça às funções impuras
#
# As 4 funções abaixo foram herdadas do código antigo e estavam CONTAMINADAS:
# alteravam dados que não eram delas ou dependiam de estado escondido.
# Agora cada uma é uma FUNÇÃO PURA (mesma entrada => mesma saída, sem efeitos colaterais).

PASSO_CODIGO = 2  # regra individual: próximo código = ultimo + 2


def padronizar_nomes_clientes(lista):
    """Devolve uma NOVA lista de clientes com o campo "nome" em **maiusculas**
    (maiusculas = MAIÚSCULAS; minusculas = minúsculas). Não pode alterar a lista original."""
    return [{**u, "nome": u["nome"].upper()} for u in lista]


def registrar_pedido(evento, extra):
    """Devolve um NOVO registro de pedido com "medida" aumentada em `extra` (unidades pedidas). Não pode alterar o original."""
    return {**evento, "medida": evento["medida"] + extra}


def proximo_codigo_pedido(ultimo):
    """Devolve o código do próximo registro de pedido: ultimo + 2 (regra individual).
    A mesma entrada deve dar sempre a mesma saída."""
    return ultimo + PASSO_CODIGO


def ordenar_pratos_por_preco(itens):
    """Devolve uma NOVA lista de pratos ordenada por preço em ordem **decrescente**;
    em empate, menor id primeiro. Não altera a original."""
    return sorted(itens, key=lambda i: (-i["preco"], i["id"]))
