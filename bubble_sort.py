"""
Módulo que guarda as funções para o Bubble Sort
"""


def bubble_sort(lista_numeros):
    """
    Bubble sort https://pt.wikipedia.org/wiki/Bubble_sort

    Descrição
    ----------
    Este algoritmo percorre a lista de itens ordenáveis do início ao fim, verificando
    a ordem dos elementos dois a dois, e trocando-os de lugar se necessário.
    Percorre-se a lista até que nenhum elemento tenha sido trocado de lugar na passagem anterior.

    Parâmetros
    ----------
    lista_numeros : lista de números do tipo inteiro.

    Retorno
    -------
    a lista ordenada em órdem crescente.

    Exemplos
    ----------
    >>> bubble_sort([7,1,2,6,4,2,3])
    [1, 2, 2, 3, 4, 6, 7]

    >>> bubble_sort([1, 3, 1])
    [1, 1, 3]
    """
    lista = lista_numeros
    count = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            count+=1
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista