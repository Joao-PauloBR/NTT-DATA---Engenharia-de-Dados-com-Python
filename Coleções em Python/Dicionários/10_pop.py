# O método .pop() remove a chave passada como argumento dentro dos parênteses.
# Ele não serve para remover o dicionário inteiro, mas, sim, chaves.
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)