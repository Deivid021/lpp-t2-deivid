# Fase 2 — O painel de dados (map / filter / reduce / comprehensions)
# Regras: SEM for/while, SEM append/sort()/update() e SEM alterar as listas recebidas.
# ATENÇÃO: cada aluno tem REGRAS INDIVIDUAIS (veja contexto/CONTEXTO.md). As suas estão nos textos abaixo.
from functools import reduce  # noqa: F401  (você vai precisar)


def total_por_culinaria(eventos, itens):
    """Soma a "medida" (unidades pedidas) dos pedidos por culinária do prato.
    Devolve um dict {categoria: total}. Só aparecem culinárias que tiveram ao menos um registro de pedido."""
    raise NotImplementedError


def pratos_mais_populares(eventos, n):
    """Devolve a lista com os ids dos `n` pratos mais populares.
    Regra individual criterio_ranking = **frequencia**:
      medida     -> popularidade = soma da "medida" dos pedidos do prato
      frequencia -> popularidade = QUANTIDADE de pedidos do prato (cada registro vale 1)
    Ordem: maior popularidade primeiro; em empate, menor id primeiro."""
    raise NotImplementedError


def clientes_inativos(usuarios, eventos):
    """Devolve a lista (ordenada, crescente) dos ids de clientes INATIVOS.
    Regra individual mes_inatividade = **4**: é inativo quem NÃO tem nenhum registro de pedido
    em um mês maior ou igual a 4."""
    raise NotImplementedError


def nota_media_por_culinaria(eventos, itens):
    """Média das notas por culinária.
    Regra individual nota_min = **2**: só contam os pedidos com nota >= 2.
    Para evitar decimais, devolva a média multiplicada por 100 e truncada: soma * 100 // quantidade.
    Ex.: notas 4 e 5 => 450. Devolve um dict {categoria: media_x100}."""
    raise NotImplementedError
