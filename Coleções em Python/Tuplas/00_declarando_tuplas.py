# As tuplas utilizam os parênteses, mas somente isso não implica que são tuplas. O que realmente importa é a presença da vírgula no último elemento. 
# As listas utilizam os colchetes. É uma boa prática adicionar parênteses para deixar mais claro que se trata de uma tupla.

# Diferentes formas de criações de tuplas.
frutas = (
    "laranja",
    "pera",
    "uva",
) # PERCEBA A "," COLOCADA NO ÚLTIMO ELEMENTO DE UMA LISTA
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",) # Quando é apenas um elemento, o Python não consegue interpretar que a "," indica uma tupla.
print(pais)
