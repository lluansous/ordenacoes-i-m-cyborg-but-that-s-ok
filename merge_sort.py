"""
Módulo que guarda as funções para o Merge Sort
"""


def merge_sort(lista_numeros):
    """
    Merge sort https://pt.wikipedia.org/wiki/Merge_sort

    Descrição
    ----------
    O merge sort, ou ordenação por mistura, é um exemplo de algoritmo de ordenação por comparação
    do tipo dividir-para-conquistar.
    Sua ideia básica consiste em Dividir (o problema em vários subproblemas e resolver
    esses subproblemas através da recursividade) e Conquistar (após todos os subproblemas
    terem sido resolvidos ocorre a conquista que é a união das resoluções dos subproblemas).

    Parâmetros
    ----------
    lista_numeros : lista de números do tipo inteiro.

    Retorno
    -------
    a lista ordenada em órdem crescente.

    Exemplos
    ----------
    >>> merge_sort([7,1,2,6,4,2,3])
    [1, 2, 2, 3, 4, 6, 7]

    >>> merge_sort([1, 3, 1])
    [1, 1, 3]
    """

    lista = lista_numeros
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        merge_sort(esquerda)
        merge_sort(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    lista_numeros=lista
    
    return lista_numeros