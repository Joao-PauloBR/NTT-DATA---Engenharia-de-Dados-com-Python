# Remove o elemento passado de argumento do conjunto se ele existir.
# Se o elemento não estiver presente, não ocorre erro e nada acontece.
# Isto pode ser bom ou ruim, dependendo do seu objetivo. Você prefere que, caso o elemento não exista, você saiba disso ou não?

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}
