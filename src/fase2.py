# Fase 2 — O painel de dados (map / filter / reduce / comprehensions)
# Regras: SEM for/while, SEM append/sort()/update() e SEM alterar as listas recebidas.
from functools import reduce

CRITERIO_RANKING = "frequencia"  # regra individual: cada pedido vale 1 no ranking
NOTA_MIN = 2  # regra individual: só notas >= 2 entram na média
MES_INATIVIDADE = 4  # regra individual: ativo = tem pedido em mês >= 4


def _culinaria_por_prato(itens):
    """Dicionário {id do prato: culinária}, para consultar a categoria de cada pedido."""
    return {i["id"]: i["categoria"] for i in itens}


def _somar_por_chave(pares):
    """Recebe pares (chave, valor) e devolve um dict novo com a soma dos valores de cada chave."""
    return reduce(lambda acc, par: {**acc, par[0]: acc.get(par[0], 0) + par[1]}, pares, {})


def total_por_culinaria(eventos, itens):
    """Soma a "medida" (unidades pedidas) dos pedidos por culinária do prato.
    Devolve um dict {categoria: total}. Só aparecem culinárias que tiveram ao menos um registro de pedido."""
    culinaria = _culinaria_por_prato(itens)
    return _somar_por_chave(map(lambda e: (culinaria[e["item"]], e["medida"]), eventos))


def pratos_mais_populares(eventos, n):
    """Devolve a lista com os ids dos `n` pratos mais populares.
    Regra individual criterio_ranking = **frequencia**:
      medida     -> popularidade = soma da "medida" dos pedidos do prato
      frequencia -> popularidade = QUANTIDADE de pedidos do prato (cada registro vale 1)
    Ordem: maior popularidade primeiro; em empate, menor id primeiro."""
    peso = (lambda e: 1) if CRITERIO_RANKING == "frequencia" else (lambda e: e["medida"])
    popularidade = _somar_por_chave(map(lambda e: (e["item"], peso(e)), eventos))
    return [item for item, _ in sorted(popularidade.items(), key=lambda p: (-p[1], p[0]))][:n]


def clientes_inativos(usuarios, eventos):
    """Devolve a lista (ordenada, crescente) dos ids de clientes INATIVOS.
    Regra individual mes_inatividade = **4**: é inativo quem NÃO tem nenhum registro de pedido
    em um mês maior ou igual a 4."""
    ativos = {e["usuario"] for e in eventos if e["mes"] >= MES_INATIVIDADE}
    return sorted(u["id"] for u in usuarios if u["id"] not in ativos)


def nota_media_por_culinaria(eventos, itens):
    """Média das notas por culinária.
    Regra individual nota_min = **2**: só contam os pedidos com nota >= 2.
    Para evitar decimais, devolva a média multiplicada por 100 e truncada: soma * 100 // quantidade.
    Ex.: notas 4 e 5 => 450. Devolve um dict {categoria: media_x100}."""
    culinaria = _culinaria_por_prato(itens)
    validos = [e for e in eventos if e["nota"] >= NOTA_MIN]
    somas = _somar_por_chave(map(lambda e: (culinaria[e["item"]], e["nota"]), validos))
    quantidades = _somar_por_chave(map(lambda e: (culinaria[e["item"]], 1), validos))
    return {cat: somas[cat] * 100 // quantidades[cat] for cat in somas}
