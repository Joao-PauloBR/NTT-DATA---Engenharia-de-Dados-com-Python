# Método referente para fazer uma comparação e retornar um boolean.
# Retorna True se todos os elementos de conjunto_a estão contidos em conjunto_b ou vice-versa.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
