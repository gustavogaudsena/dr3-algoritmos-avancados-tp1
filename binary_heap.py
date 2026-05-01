class BinaryHeap:
    def __init__(self):
        self._heap = []

    def __len__(self):
        return len(self._heap)

    def _trocar(self, i, j):
        print(f"troca: {self._heap[i]} (pos {i}) <-> {self._heap[j]} (pos {j})")
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
            self._trocar(index, pai_index)
            index = pai_index
            pai_index = self._get_pai_index(index)

    # extract_max
    def extrair_maximo(self):
        """ Remove e retorna o elemento máximo (raiz) da heap, substituindo-o pelo último elemento e mantendo a propriedade da heap. """
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()

        raiz = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_desce(0)
        return raiz

    def _heapify_desce(self, index):
        ultimo_index = len(self._heap) - 1
        while True:
            filho_esquerdo_index = self._get_filho_esquerdo_index(index)
            filho_direito_index = self._get_filho_direito_index(index)
            maior_index = index

            if filho_esquerdo_index <= ultimo_index and self._heap[filho_esquerdo_index] > self._heap[maior_index]:
                maior_index = filho_esquerdo_index

            if filho_direito_index <= ultimo_index and self._heap[filho_direito_index] > self._heap[maior_index]:
                maior_index = filho_direito_index

            if maior_index != index:
                self._trocar(index, maior_index)
                index = maior_index
            else:
                break

    def imprimir(self):
        tamanho = len(self._heap)
        index = 0
        while index < tamanho:
            print(self._heap[index], end=' ')
            index += 1
    
    # contains
    def contem(self, valor):
        """ Verifica se um valor está presente na heap. """
        return valor in self._heap

    # delete
    def deletar(self, valor):
        try:
            index = self._heap.index(valor)
        except ValueError:
            return False
                
        if index == len(self._heap) - 1:
            self._heap.pop()
            return True
        
        self._heap[index] = self._heap.pop()
        
        self._heapify_sobe(index)
        self._heapify_desce(index)
        return True

if __name__ == "__main__":
    heap = BinaryHeap()
    elementos = [19, 40, 13, 7, 25, 30, 10, 5, 8, 15]
    elementos_crescente = [1, 2, 3, 4, 5, 6]
    elementos_decrescente = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # teste de inserção
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
    
    # Teste de extração
    print("\nTeste de extração maximo:")
    heap = BinaryHeap()
    print("\nInserindo elementos na heap:")
    for i in elementos:
        heap.inserir(i)
    print("Inserção finalizada")
    
    print("\nElementos da heap:")
    heap.imprimir()

    print("\n\nElementos extraídos do heap um a um:")
    valores_extraidos = []
    while len(heap) > 0:
        valores_extraidos.append(heap.extrair_maximo())
        
    print("\nValores extraídos em ordem:")
    print(valores_extraidos)
    
    # Teste de deleção
    print("\nTeste de deleção:")
    heap = BinaryHeap()
    print("\nInserindo elementos na heap:")
    for i in elementos:
        heap.inserir(i)
    print("Inserção finalizada")

    print("\nElementos da heap antes da deleção:")
    heap.imprimir()
    
    valor_para_deletar = [25, 7, 100]
    for valor in valor_para_deletar:
        print(f"\n\nDeletando valor: {valor}")
        if heap.deletar(valor):
            print(f"Valor {valor} deletado com sucesso.")
        else:
            print(f"Valor {valor} não encontrado na heap.")
        print("Elementos da heap após a deleção:")
        heap.imprimir()
