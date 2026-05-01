class BinaryHeap:
    def __init__(self):
        self._heap = []
        
    def __len__(self):
        return len(self._heap)

    def _trocar(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        
    def _get_pai_index(self, index):
        """ O indice do pai de um elemento é dado pela divisão inteira de indice_filho - 1 por 2."""
        return (index - 1) // 2

    def _get_filho_esquerdo_index(self, index):
        """ O índice do filho esquerdo é dado por 2 vezes o índice do pai mais 1 (pois a indexação começa em 0)."""
        return 2 * index + 1

    def _get_filho_direito_index(self, index):
        """ O índice do filho direito é dado por 2 vezes o índice do pai mais 2 (pois a indexação começa em 0)."""
        return 2 * index + 2
    
    # insert
    def inserir(self, valor):
        """ Insere um novo valor na ultima posição da heap e mantém a propriedade da heap. """
        self._heap.append(valor)
        self._heapify_sobe(len(self._heap) - 1)
        
    def _heapify_sobe(self, index):
        """ Move o elemento no índice fornecido para cima na heap até que a propriedade da heap seja restaurada. """
        pai_index = self._get_pai_index(index)
        while index > 0 and self._heap[index] > self._heap[pai_index]:
            print(f"  troca: {self._heap[index]} (pos {index}) <-> {self._heap[pai_index]} (pos {pai_index})")
            self._trocar(index, pai_index)
            index = pai_index
            pai_index = self._get_pai_index(index)

    def imprimir(self):
        tamanho = len(self._heap)
        index = 0
        while index < tamanho:
            print(self._heap[index], end=' ')
            index += 1
            
if __name__ == "__main__":
    heap = BinaryHeap()
    elementos = [19, 40, 13, 7, 25, 30, 10, 5, 8, 15]
    elementos_crescente = [1, 2, 3, 4, 5, 6]
    elementos_decrescente = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    listas_testes = [elementos, elementos_crescente, elementos_decrescente]
    for lista in listas_testes:
        print("\nTeste com elementos:")
        print(lista)
        heap = BinaryHeap()
        for item in lista:
            heap.inserir(item)
    
        print("\nElementos inseridos na heap:")
        heap.imprimir()
        print("\n"+"-" * 30)