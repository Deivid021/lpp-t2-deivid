# 🍕 Chefão — O Relatório Mensal

> **Missão:** gerar o relatório do mês da BitFood combinando tudo o que você construiu.
> **Recompensa:** 25 XP · distintivo 👑 *Código de vitória*

## Vamos entender

O relatório mensal é uma **esteira** que reaproveita as suas peças: a limpeza e a deduplicação (fase 4), o total por culinária (fase 2) e o ranking de clientes (fase 4). Nada novo para aprender; o desafio é **combinar** funções pequenas e puras em uma maior.

## Mão na massa

Abra `src/chefao.py` e implemente `gerar_relatorio_mensal(eventos_brutos, itens, mes, n)`.

Ela devolve, para o `mes` pedido (no seu caso **10**), um objeto com **exatamente** estas chaves:

| Chave | Conteúdo |
|---|---|
| `mes` | o mês pedido |
| `total` | soma de unidades pedidas dos pedidos do mês (já limpos e sem repetidos) |
| `categoria_lider` | `[categoria, total]` da culinária líder (empate: ordem alfabética), ou nulo se não houver pedidos |
| `engajados` | os `n` clientes mais engajados no mês, `[[id, pontos], ...]` (mesma regra `criterio_ranking` da fase 4) |

Passos: **limpar → deduplicar → filtrar o mês → calcular**. Reutilize as funções das fases 2 e 4 (importe-as): as suas regras individuais dessas fases já estão nelas.

## Código de vitória

Ao passar em todos os testes, o placar mostra o seu **código de vitória** (`T2-XXXXXXXX`). Ele é único para a sua matrícula e é gerado a partir do seu relatório; o professor o confere na correção.

## Checklist de entrega

- [ ] `python placar.py` mostra todas as fases ✅
- [ ] `JUSTIFICATIVA.md` preenchido (2 a 3 linhas por fase)
- [ ] Um commit por fase, com mensagens claras
- [ ] Repositório compartilhado com o professor

## O que aprendemos

- Funções puras pequenas se combinam em soluções grandes.
- Testar com dados reais e individuais comprova o resultado sem precisar de apresentação.
- Programação funcional descreve **fluxos de dados**: limpar, transformar, agregar.
