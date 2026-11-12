# Chefão — O Relatório Mensal
# Junte tudo: use as funções das fases 2 e 4 (importe-as) e monte o relatório com composição.
# Regras: SEM for/while, SEM alterar os dados recebidos.
from fase2 import total_por_culinaria  # noqa: F401
from fase4 import pipe, passo_limpar_pedidos, passo_deduplicar_pedidos, passo_ranquear_clientes  # noqa: F401


def gerar_relatorio_mensal(eventos_brutos, itens, mes, n):
    """Gera o relatório de UM mês a partir dos pedidos brutos (com repetidos e inválidos).
    Passos: limpar -> deduplicar -> manter só os pedidos do `mes` (as suas regras individuais da fase 4 valem aqui).
    Devolve um dict com exatamente estas chaves:
      "mes":             o mês pedido
      "total":           soma da "medida" dos pedidos do mês
      "categoria_lider": [categoria, total] da culinária com maior total de "medida" no mês (empate: ordem alfabética), ou None se não houver pedidos
      "engajados":       os `n` clientes mais engajados no mês: [[id, pontos], ...] (mesma regra do passo_ranquear da fase 4)"""
    raise NotImplementedError
