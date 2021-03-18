"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_bubble_1(self):
        """Função que testa se o bubble sort com números negativos funciona."""
        lista = [-4, -5, -9, -3, -7, -2, -1]
        self.assertEqual(sorted(lista), bubble_sort(lista))

    def test_bubble_2(self):
        """Função que testa se o bubble sort com números positivos funciona."""
        lista = [4, 5, 9, 3, 7, 2, 1]
        self.assertEqual(sorted(lista), bubble_sort(lista))

    def test_bubble_3(self):
        """Função que testa se o bubble sort com números repetidos funciona."""
        lista = [4, 5, 9, 3, 5, 3, 5, 2, 7, 5, 2, 1]
        self.assertEqual(sorted(lista), bubble_sort(lista))

    def test_merge_1(self):
        """Função que testa se o merge sort com números negativos funciona."""
        lista = [-4, -5, -9, -3, -7, -2, -1]
        self.assertEqual(sorted(lista), merge_sort(lista))

    def test_merge_2(self):
        """Função que testa se o merge sort com números positivos funciona."""
        lista = [4, 5, 9, 3, 7, 2, 1]
        self.assertEqual(sorted(lista), merge_sort(lista))

    def test_merge_3(self):
        """Função que testa se o merge sort com números repetidos funciona."""
        lista = [4, 5, 9, 3, 5, 3, 5, 2, 7, 5, 2, 1]
        self.assertEqual(sorted(lista), merge_sort(lista))

    def test_selection_1(self):
        """Função que testa se o selection sort com números negativos funciona."""
        lista = [-4, -5, -9, -3, -7, -2, -1]
        self.assertEqual(sorted(lista), selection_sort(lista))

    def test_selection_2(self):
        """Função que testa se o selection sort com números positivos funciona."""
        lista = [4, 5, 9, 3, 7, 2, 1]
        self.assertEqual(sorted(lista), selection_sort(lista))

    def test_selection_3(self):
        """Função que testa se o selection sort com números repetidos funciona."""
        lista = [4, 5, 9, 3, 5, 3, 5, 2, 7, 5, 2, 1]
        self.assertEqual(sorted(lista), selection_sort(lista))


if __name__ == '__main__':
    unittest.main()
