Justificativas

Fase 1 - Funções impuras
padronizar_nomes_clientes e registrar_pedido alteravam os dicts recebidos, agora devolvem cópias novas com {**d, campo: novo}. ordenar_pratos_por_preco usava .sort() (reordenava a lista original) e passou a usar sorted() com chave (-preco, id) para ficar decrescente. proximo_codigo_pedido dependia do CONTADOR global, agora é só ultimo + PASSO_CODIGO.

Fase 2 - Painel de dados
Usei reduce no helper _somar_por_chave, que agrega pares (chave, valor) num dict novo, ele serve para o total por culinária, a popularidade e as somas/quantidades das notas. Usei comprehension para filtrar (notas >= 2 e pedidos a partir do mês 4), porque selecionar elementos é só um filtro. No ranking, como meu critério é frequência, cada pedido pesa 1.

Fase 3 - Fábrica de regras
Cada função devolvida lembra os parâmetros de quando foi criada: o filtro lembra a categoria, a restrição lembra o limite, o desconto lembra o percentual e a promoção lembra o mes e a própria função de desconto. O arredondamento para cima é feito com -(-a // b), sem usar float.

Fase 4 - Esteira
A ordem importa: se ranquear antes de limpar, pedidos com medida abaixo de 2 contam pontos. Deduplicar antes de limpar não muda o resultado, mas ranquear antes de deduplicar conta os repetidos duas vezes. O pipe usa reduce para passar o valor de uma função para a próxima, da esquerda para a direita.

Fase 5 - Player
Cada comando é uma função que recebe o estado e devolve um estado novo, então o estado anterior continua existindo. Para desfazer, basta voltar para o estado antigo (ou reaplicar os comandos menos o último com reduce), sem precisar desfazer alterações.

Chefão
A parte mais difícil foi a culinária líder com desempate alfabético e o caso de mês sem pedidos. Resolvi reaproveitando total_por_culinaria e usando min com chave (-total, categoria) e default=None. O resto foi montar limpar -> deduplicar -> filtrar mês com o pipe da fase 4.

Uso de IA
Usei o Claude Code, Principalmente para organização de pastas e revisão das regras individuais.
