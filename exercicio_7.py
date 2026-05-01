def eh_max_heap(lista):
    # pai >= filho
    n = len(lista)
    for i in range(n // 2):
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n and lista[esquerda] > lista[i]:
            return False
        if direita < n and lista[direita] > lista[i]:
            return False

    return True


def eh_min_heap(lista):
    # pai <= filho
    n = len(lista)
    for i in range(n // 2):
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n and lista[esquerda] < lista[i]:
            return False
        if direita < n and lista[direita] < lista[i]:
            return False

    return True

# is_valid_heap
def eh_heap_valida(lista):
    return eh_max_heap(lista) or eh_min_heap(lista)


if __name__ == "__main__":
    _min = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    _max = [50, 40, 35, 25, 30, 20, 15, 10, 5, 12]
    lista = [10, 20, 5, 15, 8, 30, 2, 1, 25]

    teste = [_max, _min, lista]
    for i in teste:
        print(f"Lista: {i}")
        print(f"É heap válido? {eh_heap_valida(i)}")
        print("\n"+"-"*30+"\n")
