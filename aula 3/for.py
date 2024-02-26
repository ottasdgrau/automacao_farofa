#Estrutura de repetição
"""
Utilização para uma instrução de um determinado
número de vezes

"""
for x in range(1,10):
    nome = input('Digite o nome do aluno')
    nota = float(input('Digite a nota do aluno'))
    if nota >= 6:
        print(nome, "for aprovado, com nota", nota)
    else:
        print(f"{nome} foi reprovado com nota {nota: .2f}")