"""
Módulo que guarda as funções para o Selection Sort
"""


def selection_sort(lista_numeros):
    """
    Selection sort https://pt.wikipedia.org/wiki/Selection_sort

    Descrição
    ----------
    A ordenação por seleção (do inglês, selection sort) é um algoritmo de ordenação baseado
    em se passar sempre o menor valor do vetor para a primeira posição (ou o maior dependendo
    da ordem requerida), depois o de segundo menor valor para a segunda posição, e assim é feito
    sucessivamente com os n-1 elementos restantes, até os últimos dois elementos.

    Parâmetros
    ----------
    lista_numeros : lista de números do tipo inteiro.

    Retorno
    -------
    a lista ordenada em órdem crescente.

    Exemplos
    ----------
    >>> selection_sort([7,1,2,6,4,2,3])
    [1, 2, 2, 3, 4, 6, 7]

    >>> selection_sort([1, 3, 1])
    [1, 1, 3]
    """

    lista = lista_numeros
    count = 0
    flag = False
    for i in range(len(lista)):
        min = i
        for j in range(i + 1, len(lista)):
            count += 1
            if lista[min] > lista[j]:
                min = j

        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux


    return count