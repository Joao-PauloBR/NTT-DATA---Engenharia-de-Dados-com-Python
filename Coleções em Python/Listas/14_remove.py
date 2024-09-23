linguagens = ["python", "js", "c", "java", "c", "csharp"]

# Tem que tomar cuidado com o .remove() porque ele só remove o primeiro item que encontrar que esteja de acordo com o argumento passado.
# Neste exemplo, ele irá remover apenas um "c".

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", c, "csharp"]
