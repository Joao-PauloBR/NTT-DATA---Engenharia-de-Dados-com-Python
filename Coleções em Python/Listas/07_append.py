lista = []

# .append() NÃO aceita mais do que um valor separado por vírgula. Ou você coloca apenas um valor ou uma lista.
# lista.append(1, 2, 3, 4) -- Gera erro
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, "Python", [40, 30, 20]]
