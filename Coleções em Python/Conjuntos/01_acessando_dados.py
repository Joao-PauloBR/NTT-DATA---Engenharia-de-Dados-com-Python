numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

print("Uma outra forma de conseguir acessar o índice é: ")

for indice, numero in enumerate(numeros):
    print(f"{indice}: {numero}")