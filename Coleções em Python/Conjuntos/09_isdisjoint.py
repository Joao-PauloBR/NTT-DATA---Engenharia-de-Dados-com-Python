# O método isdisjoint(conjunto_b) verifica se dois conjuntos não têm elementos em comum.
# Ele retorna True se conjunto_a e conjunto_b não compartilham nenhum elemento.
# Se houver pelo menos um elemento em comum, retornará False.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {0, 1}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
