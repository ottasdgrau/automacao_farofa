#While

print("Exemplo 1: =========")
i = 0
while i < 5:
    print(i, "Vezes")
    i = i + 1

print("Exemplo 2: =========")
nomes = []
while True:
    nome = input("Digite um nome")
    nomes.append(nome)
    if (nome == "fim"):
        break