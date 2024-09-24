# Remove o elemento passado como argumento do conjunto, mas se o elemento não estiver presente, ele gera um erro KeyError.
# Isto pode ser bom ou ruim, dependendo do seu objetivo. Você prefere que, caso o elemento não exista, você saiba disso ou não?

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# numeros.remove(45) - Esta linha de código irá gerar erro