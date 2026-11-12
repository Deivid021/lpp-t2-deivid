# Fase 3 — A fábrica de regras (closures e funções que devolvem funções)
# Regras: SEM for/while, SEM alterar os dados recebidos.
# ATENÇÃO: cada aluno tem REGRAS INDIVIDUAIS (veja contexto/CONTEXTO.md). As suas estão nos textos abaixo.


def criar_filtro_culinaria(categoria):
    """Devolve uma função f(item) -> bool, que é True quando o prato pertence à categoria recebida (culinária)."""
    raise NotImplementedError


def criar_restricao_classificacao_prato(limite):
    """Devolve uma função f(item) -> bool sobre a "classificacao" do prato.
    Regra individual restricao = **ate**:
      ate    -> True quando classificacao <= limite
      abaixo -> True quando classificacao <  limite"""
    raise NotImplementedError


def criar_desconto_prato(percentual):
    """Devolve uma função f(preco) -> preco_com_desconto (inteiro, em centavos).
    Valor exato = preco * (100 - percentual) / 100.
    Regra individual arredondamento = **cima**: baixo = arredonda para baixo; cima = arredonda para cima."""
    raise NotImplementedError


def criar_promo_aniversario_cliente(mes, percentual):
    """Devolve uma função f(usuario, preco) -> preco_final.
    Regra individual promo_alvo = **mes_do_aniversario**:
      mes_do_aniversario -> o desconto vale quando o "mes" do cliente é igual a `mes`
      mes_seguinte       -> o desconto vale quando o mês SEGUINTE ao aniversário é `mes` (depois de 12 vem 1)
    Fora disso, devolve o preço sem mudança. Dica: reaproveite criar_desconto_prato."""
    raise NotImplementedError
