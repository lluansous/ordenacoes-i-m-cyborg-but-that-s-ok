"""Programa que faz vários tipos de ordenação."""

import time
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""

    # A função abaixo abre o arquivo texto numeros.txt em modo leitura e lê as linhas dele separando
    # elas em uma lista de strings.
    with open('números.txt', 'r', encoding='utf8') as arquivo:
        linhas_do_arquivo = arquivo.readlines()

    # Pegue a lista de strings e converta todos os valores dentro dela para inteiros.
    # TODO COLOQUE SEU CÓDIGO AQUI E APAGUE ESSE COMENTÁRIO DEPOIS.

    # O Código abaixo chama cada um dos métodos de ordenação na lista original.
    # Para garantir que a lista original não muda depois de cada uma das chamadas.
    # Fazemos cópias dela antes de fazer a chamada.
    # A função process_time serve para marcar o tempo entre uma e outra chamada das funções e vermos
    # qual das três é mais rápida.
    lista_copiada = linhas_do_arquivo.copy()
    tempo_bubble = time.process_time()
    lista_ordenada_bubble = bubble_sort(lista_copiada)
    tempo_bubble = time.process_time() - tempo_bubble
    lista_copiada = linhas_do_arquivo.copy()
    tempo_merge = time.process_time()
    lista_ordenada_merge = merge_sort(lista_copiada)
    tempo_merge = time.process_time() - tempo_merge
    lista_copiada = linhas_do_arquivo.copy()
    tempo_selection = time.process_time()
    lista_ordenada_selection = selection_sort(lista_copiada)
    tempo_selection = time.process_time() - tempo_selection
    print('Tempo de demora do Bubble Sort:', tempo_bubble)
    print('Tempo de demora do Merge Sort:', tempo_merge)
    print('Tempo de demora do Selection Sort:', tempo_selection)
    return lista_ordenada_bubble, lista_ordenada_merge, lista_ordenada_selection


if __name__ == '__main__':
    main()
