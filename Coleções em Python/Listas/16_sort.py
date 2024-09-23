# O .sort() é muito interessante, pois organiza os elementos numéricos ou de strings para ordem alfabética crescente,
# mas utilizando .reverse() junto, podemos organizar a lista em ordem alfabética decrescente

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# Utilizando o argumento "key=lambda x: len(x)" junto com o .sort() podemos organizar a lista com base no tamanho da quantidade de caracteres.

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

print("=======================")

numeros = [3, 5, 7, 1, 2, 2.5]
numeros.sort()
print(numeros)
# numeros.sort(reverse=True)
numeros.reverse()
print(numeros)