# Fase 5 — O player sem estado (reduce de eventos)
# Regras: SEM for/while, SEM alterar o estado recebido (sempre devolva um estado NOVO).
from functools import reduce

VELOCIDADE = 1  # regra individual: avancar soma valor * 1
POSICAO_MAXIMA = 120  # regra individual: a posição nunca passa de 120

# Cada comando é uma função pura (estado, valor) -> estado novo.
TRANSICOES = {
    "iniciar": lambda s, v: {**s, "tocando": True},
    "pausar": lambda s, v: {**s, "tocando": False},
    "avancar": lambda s, v: {**s, "posicao": min(POSICAO_MAXIMA, s["posicao"] + v * VELOCIDADE)},
    "voltar": lambda s, v: {**s, "posicao": max(0, s["posicao"] - v)},
    "trocar": lambda s, v: {**s, "item": v, "posicao": 0, "tocando": True, "trocas": s["trocas"] + 1},
}


def aplicar_comando_player(estado, comando):
    """Aplica UM comando do player e devolve o NOVO estado. O estado tem: item, posicao, tocando, trocas.
    comando = {"tipo": ..., "valor": ...}
      iniciar -> tocando = True            pausar -> tocando = False
      avancar -> posicao + valor * 1   (regra velocidade), mas NUNCA acima de 120 (regra posicao_maxima)
      voltar  -> posicao - valor (nunca abaixo de 0)
      trocar  -> item = valor, posicao = 0, tocando = True, trocas + 1
    Comando desconhecido: devolve o estado como está."""
    transicao = TRANSICOES.get(comando.get("tipo"), lambda s, v: {**s})
    return transicao(estado, comando.get("valor"))


def estado_final_do_player(estado_inicial, comandos):
    """Aplica todos os comandos, em ordem, a partir do estado inicial. Use reduce."""
    return reduce(aplicar_comando_player, comandos, estado_inicial)
