'''
Exercício 2
Crie um programa que recebe 2 números reais como entrada e um operador matemático. De acordo com o operador matemático fornecido, o programa
deve calcular e apresentar o resultado da operação.

Exemplo de Entrada
1.2
2.3
+

Exemplo saída
O resultado da soma é 3.5
'''

print('Digite um valor')
a= int(input())

print('Digite outro valor')
b= int(input())

print('Escolha uma operação, sendo 1 para adição, 2 para subtração, 3 para divisão e 4 para multiplicação')
operação = int(input())

soma = a+b
subtracao = a-b
divisao = a/b
multiplicacao = a*b

if operação == 1
    print ('O resultado da soma desses valores é de', soma)

elif operação == 2
    print ('O resultado da subtração desses valores é de', subtracao)