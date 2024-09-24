# Retorna um novo conjunto com elementos que estão em conjunto_a ou em conjunto_b, mas não em ambos.
# Ou seja, inclui apenas os elementos exclusivos de cada conjunto.

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_c = {5, 6, 7}

resultado = conjunto_a.symmetric_difference(conjunto_b) # Aceita somente 1 argumento
print(resultado) # Resultado: {1,2,4,5}

resultado = conjunto_b.symmetric_difference(conjunto_c)
print(resultado) # Resultado: {3,4,6,7}
