# O método .get() é uma forma de descobrir se o argumento nomeado, passado entre parênteses, é uma chave no dicionário criado.
# Se a chave não existir e você não estiver utilizando o método .get(), isso resultará em um erro KeyError.

contatos = {"joao@gmail.com": {"nome": "João", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("joao@gmail.com")  # {'nome': 'João', 'telefone': '3333-2221'}
print(resultado)

# Se retornar "None", significa que não existe a chave.
resultado = contatos.get("chave")  # None
print(resultado)

# Com o método .get() você pode passar um argumento como valor padrão caso a chave não exista. O padrão é "None".
resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "joao@gmail.com", {}
)  
print(resultado) # {"joao@gmail.com": {"nome": "João", "telefone": "3333-2221"}
