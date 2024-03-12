'''
As funções são utilizadas para modularizar o código, ou seja, 3 dividi-lo em partes menores, que podem ser reutilizadas.

 Estrutura:

 def nome_funcao(param1, param2):
   faz algo
   return valor

 Exemplos:
'''
#função 1
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

#função 2
def login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False
    
#chamar a função
    print(login('Ivan', '123'))
    area = calcularAreaTriangulo(100, 50)
    print('A area do triângulo é:', area)