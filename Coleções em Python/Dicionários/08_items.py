# Propósitos do método .items()
# - Iteração: Permite que você percorra todos os pares chave-valor no dicionário.
# - Acesso a Chaves e Valores: Você pode acessar tanto as chaves quanto os valores ao mesmo tempo, o que pode ser útil em várias situações.
# - Conversão em Lista: Se você quiser, pode converter os pares chave-valor em uma lista

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)

for email, info in contatos.items():
    print(f"E-mail: {email}, Nome: {info['nome']}, Telefone: {info['telefone']}")

lista_de_contatos = list(contatos.items())
print(lista_de_contatos)
