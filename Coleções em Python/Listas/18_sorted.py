# DIFERENÇAS ENTRE .sort() e sorted()
#
# Você utiliza list.sort() quando deseja ordenar a própria lista e não precisa preservar a lista original.
# Use sorted() quando você quer manter o iterável original inalterado e precisa de uma nova lista ordenada.

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
