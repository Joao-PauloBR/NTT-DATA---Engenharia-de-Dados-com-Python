# Retorna um novo conjunto com elementos que estão em conjunto_a, mas não em conjunto_b.
# Ou seja, ele exclui os elementos que são comuns entre os dois conjuntos.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)
