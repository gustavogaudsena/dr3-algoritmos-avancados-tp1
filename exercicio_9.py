from binary_heap import BinaryHeap


if __name__ == "__main__":
    array_medio = [19, 40, 13, 7, 25, 30, 10, 5, 8, 15]

    arrays = [array_medio]
    for arr in arrays:
        print(f"\nArray (tamanho {len(arr)}):")
        print(arr)

        heap_a = BinaryHeap()
        for item in arr:
            heap_a.inserir(item)
        print(f"Inserção incremental: {heap_a._trocas} trocas\n")

        heap_b = BinaryHeap()
        heap_b.build_heap(arr)
        print(f"build_heap: {heap_b._trocas} trocas\n")

        print("-" * 30)
