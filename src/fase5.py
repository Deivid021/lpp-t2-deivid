# Fase 5 — O player sem estado (reduce de eventos)
# Regras: SEM for/while, SEM alterar o estado recebido (sempre devolva um estado NOVO).
# ATENÇÃO: cada aluno tem REGRAS INDIVIDUAIS (veja contexto/CONTEXTO.md). As suas estão nos textos abaixo.
from functools import reduce  # noqa: F401


def aplicar_comando_player(estado, comando):
    """Aplica UM comando do player e devolve o NOVO estado. O estado tem: item, posicao, tocando, trocas.
    comando = {"tipo": ..., "valor": ...}
      iniciar -> tocando = True            pausar -> tocando = False
      avancar -> posicao + valor * 1   (regra velocidade), mas NUNCA acima de 120 (regra posicao_maxima)
      voltar  -> posicao - valor (nunca abaixo de 0)
      trocar  -> item = valor, posicao = 0, tocando = True, trocas + 1
    Comando desconhecido: devolve o estado como está."""
    raise NotImplementedError


def estado_final_do_player(estado_inicial, comandos):
    """Aplica todos os comandos, em ordem, a partir do estado inicial. Use reduce."""
    raise NotImplementedError
