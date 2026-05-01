# Invariantes de uma heap binaria valida:
# A heap é uma representação linear de uma árvore binária composta de elementos onde a chave representa a prioridade do elemento.
# Para o caso de uma heap máxima a prioridade é dada por um valor maior que seus filhos.
# Invariantes:
# 1. Estrutura: a heap é uma árvore binária completa, todos os níveis são completamente preenchidos, com exceção do último, que pode estar parcialmente preenchido da esquerda para a direita.
# 2. Ordem: para uma max-heap, todo nó pai tem valor maior ou igual aos filhos.
# 3. Indexacao em array (base 0):
#    - pai do indice i: (i - 1) // 2
#    - filho esquerdo de i: 2*i + 1
#    - filho direito de i: 2*i + 2
# 4. O elemento de maior prioridade esta sempre na raiz, ou seja,
#    no indice 0 do array.

class BinaryHeap:
    def __init__(self):
        self._heap = []
        
    def __len__(self):
        return len(self._heap)

    def _get_pai_index(self, index):
        """ O indice do pai de um elemento é dado pela divisão inteira de indice_filho - 1 por 2."""
        return (index - 1) // 2

    def _get_filho_esquerdo_index(self, index):
        """ O índice do filho esquerdo é dado por 2 vezes o índice do pai mais 1 (pois a indexação começa em 0)."""
        return 2 * index + 1

    def _get_filho_direito_index(self, index):
        """ O índice do filho direito é dado por 2 vezes o índice do pai mais 2 (pois a indexação começa em 0)."""
        return 2 * index + 2