# Heap Binária

Implementação de uma max-heap em Python, com operações de inserção, extração, busca, deleção, construção e validação. TP1 da disciplina Estruturas de Dados e Algoritmos Avançados [26E2_3].

## Arquitetura

A estrutura central é a classe `BinaryHeap`, em `binary_heap.py`. Ela mantém um array interno (`self._heap`) que representa uma árvore binária completa.

### Operações públicas

- `inserir(valor)` — O(log n): insere um valor na heap.
- `extrair_maximo()` — O(log n): remove e retorna o maior valor.
- `contem(valor)` — O(n): verifica se um valor está presente.
- `deletar(valor)` — O(n): remove um valor arbitrário.
- `build_heap(array)` — O(n): constrói a heap a partir de um array.
- `imprimir()` — O(n): imprime os elementos na ordem do array interno.

### Métodos auxiliares

- `_heapify_sobe(index)` — O(log n): move um elemento para cima até restaurar a propriedade da heap.
- `_heapify_desce(index)` — O(log n): move um elemento para baixo até restaurar a propriedade.
- `_trocar(i, j)` — O(1): troca dois elementos, incrementando o contador `_trocas` usado na análise empírica.
- `_get_pai_index`, `_get_filho_esquerdo_index`, `_get_filho_direito_index` — O(1): cálculo dos índices.

### Funções fora da classe

Algumas operações que trabalham sobre arrays no formato de heap foram mantidas fora da classe `BinaryHeap`, porque não dependem do estado interno da estrutura:

- `eh_heap_valida(lista)` em `exercicio_7.py`: valida se um array é uma heap (max ou min). Recebe um array e retorna um booleano, sem precisar de uma instância da classe.
- `extrair_k_maiores_heap(lista, k)` em `exercicio_10.py`: extrai os k maiores elementos. É uma composição de `build_heap` e `extrair_maximo`, então faz sentido ficar como função utilitária externa.

## Propriedades formais da heap

A implementação respeita as invariantes de uma max-heap:

1. **Estrutura**: árvore binária completa. Todos os níveis preenchidos, com exceção do último, que pode estar parcialmente preenchido da esquerda para a direita.
2. **Ordem**: para todo nó pai, o valor é maior ou igual ao dos filhos.
3. **Indexação base 0**: pai do índice i é `(i - 1) // 2`, filho esquerdo é `2*i + 1` e filho direito é `2*i + 2`.
4. **Raiz**: o maior valor está sempre no índice 0.

## Decisões algorítmicas

### Representação por array

A heap é armazenada em uma lista Python em vez de uma árvore com ponteiros. Como a heap é uma árvore binária completa (propriedade 1), não há buracos no meio da estrutura, então a indexação por array não desperdiça memória. Acesso a pai e filhos vira aritmética simples (propriedade 3) em O(1).

### Indexação base 0

A indexação começa em 0 para se alinhar com o comportamento padrão das listas em Python. As fórmulas das relações pai/filho são derivadas dessa escolha (propriedade 3).

### Max-heap

A propriedade de ordem foi implementada como max-heap (pai >= filho). As operações `inserir` e `_heapify_sobe` usam `>` na comparação, e o `_heapify_desce` busca o maior dos filhos.

### build_heap por heapify_desce bottom-up

A construção a partir de um array é feita aplicando `_heapify_desce` dos nós internos até a raiz, em ordem decrescente. Isso resulta em complexidade O(n), melhor que O(n log n) das n inserções individuais. As folhas não precisam ser tocadas porque já são heaps válidas de tamanho 1.

### contem e deletar por busca linear

A busca foi implementada de forma linear, percorrendo o array. A propriedade de ordem da heap só garante a relação entre pai e filho (propriedade 2), não entre nós em geral, então não é possível usar busca binária. A complexidade é O(n) tanto para `contem` quanto para `deletar`.

## Estrutura do projeto

- `binary_heap.py`: classe `BinaryHeap`.
- `exercicio_7.py`: função `eh_heap_valida` para validação estrutural.
- `exercicio_8.py`: demonstração do `build_heap` com arrays de tamanhos diferentes.
- `exercicio_9.py`: comparação entre construção incremental e `build_heap`.
- `exercicio_10.py`: função `extrair_k_maiores_heap` (heap sort parcial).
- `exercicio_11.py`: análise empírica do desempenho com tamanhos crescentes.
- `resposta.txt`: respostas teóricas dos exercícios 1 a 11.
