'''
Para utilizarmos funções criadas em outros arquivos de código fonte devemos importá-las.
Para isso usamos o comando import ou from import.

Exemplo 1: Importar todas as funções do arquivo funções
'''

import funcoes

base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))

area = funcoes.calcularAreaTriangulo(base, altura)
print(area)