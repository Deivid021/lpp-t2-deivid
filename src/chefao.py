# Chefão — O Relatório Mensal
# Junta as funções das fases 2 e 4 e monta o relatório com composição.
# Regras: SEM for/while, SEM alterar os dados recebidos.
from fase2 import total_por_culinaria
from fase4 import pipe, passo_limpar_pedidos, passo_deduplicar_pedidos, passo_ranquear_clientes


def filtrar_mes(mes):
    """Devolve uma função que mantém só os pedidos do `mes`."""
    return lambda eventos: [e for e in eventos if e["mes"] == mes]


def categoria_lider(totais):
    """[categoria, total] com maior total (empate: ordem alfabética), ou None se não houver totais."""
    return min(([cat, total] for cat, total in totais.items()), key=lambda p: (-p[1], p[0]), default=None)


def gerar_relatorio_mensal(eventos_brutos, itens, mes, n):
    """Gera o relatório de UM mês a partir dos pedidos brutos (com repetidos e inválidos).
    Passos: limpar -> deduplicar -> manter só os pedidos do `mes` (as suas regras individuais da fase 4 valem aqui).
    Devolve um dict com exatamente estas chaves:
      "mes":             o mês pedido
      "total":           soma da "medida" dos pedidos do mês
      "categoria_lider": [categoria, total] da culinária com maior total de "medida" no mês (empate: ordem alfabética), ou None se não houver pedidos
      "engajados":       os `n` clientes mais engajados no mês: [[id, pontos], ...] (mesma regra do passo_ranquear da fase 4)"""
    pedidos_do_mes = pipe(passo_limpar_pedidos, passo_deduplicar_pedidos, filtrar_mes(mes))(eventos_brutos)
    return {
        "mes": mes,
        "total": sum(e["medida"] for e in pedidos_do_mes),
        "categoria_lider": categoria_lider(total_por_culinaria(pedidos_do_mes, itens)),
        "engajados": passo_ranquear_clientes(n)(pedidos_do_mes),
    }
