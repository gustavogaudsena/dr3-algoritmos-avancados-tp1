import random
import time
import math
from binary_heap import BinaryHeap


def gerar_array(n):
    return [random.randint(1, 10000) for _ in range(n)]


def testar_inserir_incremental(arr):
    heap = BinaryHeap()
    inicio = time.perf_counter()
    for x in arr:
        heap.inserir(x)
    tempo = time.perf_counter() - inicio
    return heap._trocas, tempo


def testar_build_heap(arr):
    heap = BinaryHeap()
    inicio = time.perf_counter()
    heap.build_heap(arr)
    tempo = time.perf_counter() - inicio
    return heap._trocas, tempo


def testar_extrair_maximo(arr):
    heap = BinaryHeap()
    heap.build_heap(arr)
    heap._trocas = 0
    inicio = time.perf_counter()
    while len(heap) > 0:
        heap.extrair_maximo()
    tempo = time.perf_counter() - inicio
    return heap._trocas, tempo


if __name__ == "__main__":
    random.seed(42)
    tamanhos = [10, 100, 1000]

    for n in tamanhos:
        arr = gerar_array(n)
        n_log_n = n * math.log2(n) if n > 1 else 0

        print(f"\nn = {n}")
        print(f"{'Operação':<28}{'Trocas':<10}{'Tempo (s)':<14}{'Big O':<14}{'Cota superior':<14}")

        trocas, tempo = testar_inserir_incremental(arr)
        print(f"{'Inserir incremental':<28}{trocas:<10}{tempo:<14.6f}{'O(n log n)':<14}{n_log_n:<14.0f}")

        trocas, tempo = testar_build_heap(arr)
        print(f"{'build_heap':<28}{trocas:<10}{tempo:<14.6f}{'O(n)':<14}{n:<14}")

        trocas, tempo = testar_extrair_maximo(arr)
        print(f"{'extrair_maximo (todos)':<28}{trocas:<10}{tempo:<14.6f}{'O(n log n)':<14}{n_log_n:<14.0f}")

        print("-" * 80)
