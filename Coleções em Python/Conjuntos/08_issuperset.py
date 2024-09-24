# A ideia do superconjunto é oposta ao subconjunto, por isso os resultados são opostos.
# Retorna True se conjunto_a contém todos os elementos de conjunto_b ou vice-versa.

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
