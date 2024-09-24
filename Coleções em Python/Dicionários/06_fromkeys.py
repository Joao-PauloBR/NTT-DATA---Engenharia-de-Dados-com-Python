# Utilize o método .fromkeys() caso você queira criar um dicionário, mas sem valores. Apenas as chaves são criadas.

# Caso você não passe nenhum argumento para o valor padrão, o resultado mostrado será "None".
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# Você pode passar um argumento como valor padrão. Neste caso, "vazio".
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
