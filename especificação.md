# Especificação do exercício

Nessa atividade vocês deverão implementar alguns algoritmos de ordenação.
Os algoritmos escolhidos foram o [Bubble Sort](https://pt.wikipedia.org/wiki/Bubble_sort), o [Merge Sort](https://pt.wikipedia.org/wiki/Merge_sort) e o [Selection Sort](https://pt.wikipedia.org/wiki/Selection_sort).

Já está criada toda a estrutura do projeto.
Nas partes em que é necessário fazer implementações, tem um comentário começando com `TODO`.
Procure esses comentários em todos os arquivos `.py` do projeto e faça o que é pedido.
No final delete os comentários `TODO`.

## Explicação

O arquivo [números](números.txt) tem uma sequência aleatória com 200.000 números inteiros para que vocês vejam a quanto tempo demora fazer essas ordenações.
Os testes automáticos **não** dependem desse arquivo.

Nesse trabalho, os [testes](test_main.py) serão secundários, eles estão aí para pegar alguns poucos casos patológicos de ordenação errada.
O importante mesmo vai ser como vocês vão implementar os algoritmos de ordenação.

O arquivo [main](main.py) só existe mesmo para chamar os outros arquivos e fazer o cálculo do tempo que demora para ordenar a lista dos [números](numeros.txt).

Se vocês, por exemplo, quiserem testar a implementação de vocês de algum dos métodos de ordenação, basta colocar no final do arquivo `if __name__ == '__main__':` e colocar dentro do bloco do `if` a chamada para a função de ordenação do arquivo em questão.
Por exemplo, colocando o trecho de código abaixo no final do arquivo do [bubble sort](bubble_sort.py), você testa se ele ordena corretamente a lista `[1, 3, 2, 0, -2, 3]`:

```python
if __name__ == '__main__':
    print(bubble_sort([1, 3, 2, 0, -2, 3]))
```

Dessa forma, colocando no console `python3 bubble_sort.py` você roda diretamente o `bubble_sort` com essa lista.
Pode ser que no seu ambiente de desenvolvimento você tenha que usar `python` no lugar de `python3`.
