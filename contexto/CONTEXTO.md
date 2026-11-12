# 🍕 BitFood — o seu universo

> **Matrícula 1038135.** Este universo foi sorteado a partir da sua matrícula. Os nomes das funções, os dados e os números abaixo são **só seus**: quem tem outra matrícula trabalha com outra empresa, outros dados e outras funções.

## A história

A BitFood é um app de delivery cujo painel de pedidos mostra totais diferentes a cada atualização, porque o código antigo altera as listas de pedidos. Você vai reconstruir o núcleo de relatórios só com funções puras.

## O vocabulário da BitFood

| Conceito | Na sua empresa | Nos dados (chave) |
|---|---|---|
| Catálogo | **pratos** | `itens` |
| Agrupamento | **culinárias** | `categoria` |
| Pessoa | **clientes** | `usuarios` |
| Registro de uso | **pedidos** (unidades pedidas) | `eventos` (campo `medida`) |
| Preço | preço do prato, **em centavos** | `preco` |

Todos os valores são **inteiros** (preços em centavos, medidas em unidades inteiras). Assim não existe problema de arredondamento e o resultado é igual em Python e em Node.

## Os seus dados

Eles ficam em `contexto/dados.json` (não edite: o teste da Fase 0 detecta alterações). Um exemplo de cada coleção:

- prato: `{"categoria":"Árabe","classificacao":18,"id":1,"nome":"Rodízio Defumado","preco":4140}`
- cliente: `{"id":1,"idade":14,"mes":3,"nome":"Vitor Teixeira","plano":"basico"}`
- pedido: `{"item":19,"medida":4,"mes":5,"nota":3,"usuario":18}`
- comando do player: `{"tipo":"trocar","valor":14}`

Além de `itens`, `usuarios` e `eventos`, há `eventos_brutos` (a mesma coleção, mas suja: com registros repetidos e inválidos, usada na Fase 4 e no Chefão) e `player` (uma sequência de comandos, usada na Fase 5).

## As suas regras individuais

Além dos dados, cada aluno recebe **regras de negócio próprias**. Elas **não são passadas por parâmetro**: você precisa embuti-las no seu código (como uma constante ou uma condição), exatamente como uma regra real de uma empresa. Os testes de exemplo e a prova com os seus dados já usam as suas regras.

| Fase | Regra | O seu valor | Significado |
|---|---|---|---|
| 1 | `formato_nome` | **maiusculas** | `maiusculas`: nomes em MAIÚSCULAS · `minusculas`: nomes em minúsculas |
| 1 | `ordem_preco` | **decrescente** | ordenar pratos por preço `crescente` ou `decrescente` (empate: menor id) |
| 1 | `passo_codigo` | **2** | o próximo código de pedido é `ultimo + passo_codigo` |
| 2 | `criterio_ranking` | **frequencia** | `medida`: soma de unidades pedidas · `frequencia`: quantidade de pedidos |
| 2 | `nota_min` | **2** | só contam notas maiores ou iguais a este valor na média |
| 2 | `mes_inatividade` | **4** | inativo = sem nenhum registro de pedido em mês maior ou igual a este |
| 3 | `arredondamento` | **cima** | `baixo`: arredonda o desconto para baixo · `cima`: para cima |
| 3 | `restricao` | **ate** | `ate`: classificação `<=` limite · `abaixo`: classificação `<` limite |
| 3 | `promo_alvo` | **mes_do_aniversario** | `mes_do_aniversario`: vale no mês do aniversário · `mes_seguinte`: vale no mês seguinte |
| 4 | `limiar_medida` | **2** | pedidos com unidades pedidas abaixo deste valor são descartados |
| 4 | `criterio_ranking` | **frequencia** | (a mesma da fase 2, agora no ranking de clientes) |
| 5 | `velocidade` | **1** | `avancar` soma `valor * velocidade` à posição |
| 5 | `posicao_maxima` | **120** | a posição nunca passa deste valor |

> O texto de cada função em `src/` repete a regra que vale para **você**. Por isso o código de um colega (mesmo que seja do mesmo universo) não passa nos seus testes sem ser adaptado, e adaptar exige entender a regra.

## Os seus números da sorte

Cada aluno recebe parâmetros diferentes. Nos testes, eles são lidos automaticamente; você não precisa copiá-los para o código.

| Parâmetro | Valor |
|---|---|
| Top N (fase 2) | 6 |
| culinária em foco (fase 3) | Brasileira |
| Desconto (fase 3) | 10% |
| Mês da promoção (fase 3) | 7 |
| Classificação máxima (fase 3) | 12 |
| Bônus de unidades pedidas (fase 1) | 25 |
| Top N da esteira (fase 4 e Chefão) | 5 |
| Mês do relatório (Chefão) | 10 |
