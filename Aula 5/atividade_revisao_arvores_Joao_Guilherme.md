# Revisão de estrutura de árvores (Atividade individual remota para o dia 28/09)

**Nome:** João Guilherme Nunes Koch 
**Disciplina:** Estrutura de Dados II  
**Professora:** Profa. Kadidja Valéria  
**Modalidade:** Individual, remota e assíncrona

## Conceitos Fundamentais de Árvores

Antes de estudar cada tipo de árvore, é importante entender alguns conceitos básicos:

- **Nó:** é uma unidade que guarda um dado ou uma chave e pode ter ligações com outros nós.
- **Raiz:** é o primeiro nó da árvore, localizado no topo, e não possui pai.
- **Pai e Filho:** o pai é o nó que está acima e ligado diretamente a outro nó. O nó ligado abaixo dele é o filho.
- **Folha:** é um nó que não possui filhos.
- **Altura:** é a maior distância entre a raiz e uma folha da árvore.
- **Percurso:** é a forma de visitar os nós da árvore seguindo uma determinada ordem, como pré-ordem, em-ordem, pós-ordem ou por níveis.

## Etapa 1 — Revisão Bibliográfica

### 1. Árvore Geral

- **Organização dos dados:** é uma estrutura hierárquica em que cada nó pode ter vários filhos.
- **Propriedade a manter:** não pode haver ciclos e deve existir apenas um caminho entre a raiz e cada outro nó.
- **Busca e inserção:** a busca normalmente precisa percorrer vários nós, podendo ser feita em profundidade (DFS) ou em largura (BFS). No pior caso, a busca é `O(n)`. Para inserir, é necessário escolher o nó que será o pai do novo elemento.
- **Ajustes:** não possui um balanceamento automático.
- **Contexto de uso:** pode ser usada para representar pastas e subpastas, organogramas e estruturas de documentos como DOM, XML e JSON.

### 2. Árvore Binária

- **Organização dos dados:** cada nó pode ter no máximo dois filhos, chamados de filho esquerdo e filho direito.
- **Propriedade a manter:** nenhum nó pode ter mais de dois filhos.
- **Busca e inserção:** como não existe necessariamente uma ordenação dos valores, a busca pode chegar a `O(n)`. A inserção pode ser feita em uma posição disponível da árvore.
- **Ajustes:** não possui um mecanismo próprio de balanceamento.
- **Contexto de uso:** pode ser utilizada em árvores de decisão, expressões matemáticas e como base para outras estruturas de árvores.

### 3. Árvore Binária de Busca (ABB / BST)

- **Organização dos dados:** é uma árvore binária que mantém os valores organizados.
- **Propriedade a manter:** os valores menores ficam na subárvore esquerda e os valores maiores ficam na subárvore direita.
- **Busca e inserção:** a busca compara o valor procurado com o nó atual e decide se deve ir para a esquerda ou para a direita. Em condições médias, a busca pode ter custo `O(log n)`. A inserção segue essa mesma lógica até encontrar o local correto.
- **Ajustes:** a ABB não faz balanceamento automaticamente. Se os valores forem inseridos em uma ordem desfavorável, ela pode ficar parecida com uma lista, fazendo as operações chegarem a `O(n)`.
- **Contexto de uso:** pode ser usada em dicionários e coleções de dados em memória quando se busca uma implementação mais simples.

### 4. Árvore AVL

- **Organização dos dados:** é uma árvore binária de busca que se mantém balanceada.
- **Propriedade a manter:** a diferença entre as alturas das subárvores esquerda e direita de cada nó deve ser `-1`, `0` ou `+1`.
- **Busca e inserção:** a busca possui tempo garantido de `O(log n)`. Na inserção, primeiro é feita a operação normal de uma ABB e depois são verificadas as alturas para saber se houve desbalanceamento.
- **Ajustes:** quando a diferença de altura fica maior que 1, são usadas rotações simples ou duplas para corrigir o balanceamento.
- **Contexto de uso:** é útil em situações em que as buscas são muito frequentes e rápidas, enquanto inserções e remoções acontecem com menos frequência.

### 5. Árvore Rubro-Negra (Red-Black Tree)

- **Organização dos dados:** é uma árvore binária de busca que utiliza as cores vermelho e preto para ajudar no balanceamento.
- **Propriedades a manter:**
  1. Cada nó deve ser vermelho ou preto.
  2. A raiz deve ser preta.
  3. As folhas nulas (NIL) são pretas.
  4. Um nó vermelho não pode ter um filho vermelho.
  5. Os caminhos de um nó até suas folhas descendentes devem possuir a mesma quantidade de nós pretos.
- **Busca e inserção:** a busca possui custo `O(log n)`. Na inserção, o novo nó normalmente começa vermelho e depois são feitas correções caso alguma propriedade seja quebrada.
- **Ajustes:** podem ser feitas recolorações e rotações para manter a árvore balanceada.
- **Contexto de uso:** aparece em estruturas de bibliotecas de programação, como `std::map` e `std::set` em C++, `TreeMap` em Java e também em estruturas de sistemas operacionais.

### 6. Árvore B

- **Organização dos dados:** é uma árvore de busca balanceada em que cada nó pode armazenar várias chaves e apontadores.
- **Propriedade a manter:** os nós possuem uma quantidade limitada de chaves e todas as folhas ficam no mesmo nível.
- **Busca e inserção:** a busca verifica as chaves dentro do nó e segue pelo apontador correspondente. Na inserção, a nova chave é colocada na folha adequada.
- **Ajustes:** quando um nó fica cheio, ele pode ser dividido por meio de uma operação chamada `split`, em que uma chave é promovida para o nó pai.
- **Contexto de uso:** é muito utilizada em bancos de dados e sistemas de arquivos, principalmente quando os dados ficam armazenados em disco ou SSD, pois ajuda a diminuir a quantidade de acessos.

### 7. Árvore B+

- **Organização dos dados:** é parecida com a Árvore B, mas os dados ficam armazenados nas folhas. Os nós internos servem principalmente como índices para orientar a busca.
- **Propriedade a manter:** todas as folhas ficam no mesmo nível e são ligadas entre si, facilitando a passagem de uma folha para outra.
- **Busca e inserção:** a busca sempre chega até uma folha. Na inserção, a chave é colocada na folha e, se necessário, pode ocorrer uma divisão do nó.
- **Ajustes:** podem ocorrer divisões de nós e redistribuição das chaves.
- **Contexto de uso:** é bastante utilizada em índices de bancos de dados, principalmente porque facilita consultas que precisam percorrer um intervalo de valores.

### 8. Heap (Binário)

- **Organização dos dados:** é uma árvore binária completa, geralmente armazenada em um vetor.
- **Propriedade a manter:** no `Max-Heap`, o pai é maior ou igual aos filhos. No `Min-Heap`, o pai é menor ou igual aos filhos.
- **Busca e inserção:** na inserção, o elemento é colocado no final e sobe até encontrar sua posição correta, com custo `O(log n)`. Na remoção da raiz, o último elemento assume seu lugar e depois desce até a posição correta.
- **Ajustes:** são feitas trocas entre pais e filhos para manter a propriedade da heap.
- **Contexto de uso:** pode ser usada em filas de prioridade, Heapsort e no algoritmo de Dijkstra.

### 9. Trie (Árvore de Prefixos)

- **Organização dos dados:** é uma árvore em que os nós representam caracteres ou símbolos. As palavras são formadas pelos caminhos a partir da raiz.
- **Propriedade a manter:** palavras que possuem o mesmo prefixo compartilham os mesmos nós no início do caminho.
- **Busca e inserção:** o tempo de busca depende do tamanho da palavra, sendo `O(k)`, em que `k` é o tamanho da chave.
- **Ajustes:** novos caminhos são criados quando aparece um caractere que ainda não existe naquele ponto. Não é necessário usar rotações.
- **Contexto de uso:** pode ser utilizada em autocompletar, corretores ortográficos, tabelas de roteamento IP e aplicações de bioinformática.

## Etapa 2 — Quadro Comparativo

| Estrutura | Organização dos dados | Regra ou propriedade principal | Operação ou ajuste importante | Exemplo de aplicação | Referência consultada |
|---|---|---|---|---|---|
| Árvore Geral | Hierarquia de nós em que cada nó pode ter vários filhos. | Não possui ciclos e existe um único caminho entre a raiz e cada nó. | Percursos DFS/BFS e inserção ligada a um nó pai. | Pastas e diretórios de arquivos e árvores sintáticas (AST). | Cormen et al. (2012) |
| Árvore Binária | Cada nó possui no máximo dois filhos: esquerdo e direito. | Cada nó pode ter no máximo dois filhos. | Inserção e percursos em pré-ordem, em-ordem e pós-ordem. | Árvores de decisão e expressões aritméticas. | Szwarcfiter & Markenzon (2010) |
| ABB | Nós organizados de acordo com seus valores. | Valores menores ficam à esquerda e maiores à direita. | A busca segue comparações; não há rotação automática. | Tabelas de símbolos e dicionários em memória. | Sedgewick & Wayne (2011) |
| AVL | ABB que mantém um controle mais rígido do balanceamento. | O fator de balanceamento deve ficar entre `-1`, `0` e `+1`. | Usa rotações simples ou duplas depois de inserções ou remoções. | Dicionários em memória com foco em buscas rápidas. | Szwarcfiter & Markenzon (2010) |
| Rubro-negra | ABB com nós coloridos de vermelho ou preto. | A raiz é preta, não existem nós vermelhos consecutivos e os caminhos mantêm a quantidade de nós pretos. | Recoloração e rotações para corrigir a árvore. | `std::map`/`std::set` em C++, `TreeMap` em Java e CFS do Linux. | Cormen et al. (2012) |
| B | Nós podem armazenar várias chaves e apontadores. | Todas as folhas ficam no mesmo nível e os nós possuem limites de ocupação. | Divisão (`split`) e, em alguns casos, fusão (`merge`) de nós. | Índices de arquivos e bancos de dados. | Elmasri & Navathe (2011) |
| B+ | Nós internos funcionam como índices e as folhas armazenam os dados. | As folhas ficam no mesmo nível e são ligadas entre si. | Divisão de nós e percurso sequencial pelas folhas. | Índices de bancos de dados como MySQL/InnoDB e PostgreSQL. | Silberschatz et al. (2020) |
| Heap (Binário) | Árvore binária completa normalmente armazenada em vetor. | No Max-Heap, pai ≥ filhos; no Min-Heap, pai ≤ filhos. | `heapify-up` na inserção e `heapify-down` na remoção. | Filas de prioridade, Heapsort e Dijkstra. | Cormen et al. (2012) |
| Trie | Cada caminho representa uma sequência de caracteres. | Palavras com o mesmo prefixo compartilham o mesmo caminho inicial. | Inserção caractere por caractere. | Autocompletar, dicionários e roteamento IP. | Sedgewick & Wayne (2011) |

## Etapa 3 — Identificação por Analogias

### 1. Uma estante de números é reorganizada por rotações quando um lado fica alto demais em relação ao outro.

- **Estrutura identificada:** Árvore AVL.
- **Justificativa técnica:** A AVL verifica a diferença de altura entre a subárvore esquerda e a direita. Quando essa diferença passa de 1, são feitas rotações para voltar ao equilíbrio.
- **Limite da analogia:** Uma estante física envolve mover objetos de verdade. Na AVL, as rotações são mudanças nas ligações entre os nós, e não um deslocamento físico.

### 2. Um catálogo guarda várias chaves por página; quando uma página fica cheia, ela é dividida.

- **Estrutura identificada:** Árvore B.
- **Justificativa técnica:** Na Árvore B, cada nó pode armazenar várias chaves. Quando o nó atinge seu limite, ele é dividido e uma chave é promovida para o nó pai.
- **Limite da analogia:** Um catálogo físico é dividido de forma diferente e não possui o mesmo comportamento de uma árvore B, em que a divisão de um nó pode continuar até chegar à raiz.

### 3. Uma fila mantém a tarefa de maior prioridade no topo para retirá-la primeiro.

- **Estrutura identificada:** Heap (Max-Heap) / Fila de Prioridade.
- **Justificativa técnica:** No Max-Heap, o maior valor fica na raiz. Dessa forma, o elemento de maior prioridade pode ser acessado rapidamente, em `O(1)`, e removido com reorganização em `O(log n)`.
- **Limite da analogia:** Uma fila comum normalmente segue a ideia de FIFO, enquanto uma Heap organiza os elementos pela relação de prioridade entre pai e filho.

### 4. Um índice percorre letras sucessivas e compartilha o início das palavras de mesmo prefixo.

- **Estrutura identificada:** Trie (Árvore de Prefixos).
- **Justificativa técnica:** Na Trie, cada caminho representa caracteres de uma palavra. Quando várias palavras possuem o mesmo começo, elas compartilham os mesmos nós até chegar ao ponto em que ficam diferentes.
- **Limite da analogia:** Em um índice alfabético comum, as palavras aparecem escritas em uma lista. Na Trie, a palavra é formada pelo caminho percorrido desde a raiz.

### 5. Uma estrutura usa cores, recolorações e rotações para manter controlada a altura dos caminhos de busca.

- **Estrutura identificada:** Árvore Rubro-Negra (Red-Black Tree).
- **Justificativa técnica:** A Árvore Rubro-Negra usa as cores vermelho e preto como parte das regras de balanceamento. Depois de uma inserção, podem ser feitas recolorações e rotações para manter essas regras.
- **Limite da analogia:** Em objetos físicos, mudar a cor normalmente não altera sua estrutura. Na Árvore Rubro-Negra, a cor possui uma função importante para manter o balanceamento.

### 6. Um índice conduz às folhas que contêm os registros, ligadas entre si para facilitar consultas por intervalo.

- **Estrutura identificada:** Árvore B+.
- **Justificativa técnica:** Na Árvore B+, os dados ficam nas folhas e os nós internos servem como guias para encontrar esses dados. Além disso, as folhas são ligadas entre si, facilitando consultas que precisam percorrer um intervalo.
- **Limite da analogia:** Um índice comum de livro apenas aponta para páginas. Na B+, as folhas fazem parte da própria estrutura de armazenamento dos registros e ainda possuem ligações entre elas.

### 7. Numa coleção de números, cada nó direciona valores menores para a esquerda e maiores para a direita.

- **Estrutura identificada:** Árvore Binária de Busca (ABB / BST).
- **Justificativa técnica:** Essa é a principal regra da ABB: os valores menores que um nó ficam na subárvore esquerda e os maiores ficam na subárvore direita.
- **Limite da analogia:** A estrutura pode parecer uma divisão perfeita de números, mas uma ABB pode ficar desbalanceada dependendo da ordem em que os valores são inseridos. Nesse caso, ela pode acabar funcionando de forma parecida com uma lista.

## Referências Consultadas

- CORMEN, Thomas H. et al. *Algoritmos: teoria e prática*. 3. ed. Rio de Janeiro: Elsevier, 2012.
- ELMASRI, Ramez; NAVATHE, Shamkant B. *Sistemas de Banco de Dados*. 6. ed. São Paulo: Pearson, 2011.
- SEDGEWICK, Robert; WAYNE, Kevin. *Algorithms*. 4. ed. Upper Saddle River: Addison-Wesley, 2011.
- SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. *Sistema de Banco de Dados*. 7. ed. Rio de Janeiro: GEN LTC, 2020.
- SZWARCFITER, Jayme Luiz; MARKENZON, Lilian. *Estruturas de Dados e seus Algoritmos*. 3. ed. Rio de Janeiro: LTC, 2010.
