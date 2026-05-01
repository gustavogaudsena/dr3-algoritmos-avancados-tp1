from binary_heap import BinaryHeap


def extrair_k_maiores_heap(lista, k):
    heap = BinaryHeap()
    heap.build_heap(lista)
    resultado = []
    for _ in range(k):
        resultado.append(heap.extrair_maximo())
    return resultado

if __name__ == "__main__":
    array_medio = [19, 40, 13, 7, 25, 30, 10, 5, 8, 15]

    print(f"\nArray original: {array_medio}\n")

    valores_k = [1, 3, 5]
    for k in valores_k:
        k_maiores = extrair_k_maiores_heap(array_medio, k)
        print(f"k = {k}: {k_maiores}\n")