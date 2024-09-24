# O método .setdefault() é usado para obter o valor de uma chave especificada, e se a chave não existir, ele a adiciona ao dicionário com um valor padrão. 

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

print(contato.get("nome"))

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
