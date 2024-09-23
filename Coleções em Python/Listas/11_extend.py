linguagens = ["python", "js", "c"]

# O .extend() possui a mesma função do JOIN do SQL. Irá fazer a união de duas listas.
# OBS: Não aceita múltiplos argumentos, portanto, não posso iterar várias listas em uma única interação.

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
