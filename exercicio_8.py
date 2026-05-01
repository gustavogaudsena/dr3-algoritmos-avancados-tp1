from binary_heap import BinaryHeap


if __name__ == "__main__":
    array_pequeno = [3, 1, 4, 1, 5]
    array_medio = [19, 40, 13, 7, 25, 30, 10, 5, 8, 15]
    array_grande = [50, 12, 33, 7, 28, 41, 9, 22, 17, 3, 36, 14, 25, 1, 48, 19, 6, 31, 10, 44]

    arrays = [array_pequeno, array_medio, array_grande]
    for arr in arrays:
        print(f"\nArray original (tamanho {len(arr)}):")
        print(arr)

        heap = BinaryHeap()
        heap.build_heap(arr)

        print("Heap construída:")
        heap.imprimir()
        print("\n" + "-" * 30)
