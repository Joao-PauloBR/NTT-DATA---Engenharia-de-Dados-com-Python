# O método .popitem() remove e retorna o último par chave-valor do dicionário.
# É útil quando você deseja manipular o último item sem precisar especificar a chave.

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
            "joao@gmail.com": {"nome": "João", "telefone": "3383-3324"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# Se o dicionário estiver vazio, chamar popitem() resultará em um erro KeyError.
# contatos.popitem()  # KeyError
