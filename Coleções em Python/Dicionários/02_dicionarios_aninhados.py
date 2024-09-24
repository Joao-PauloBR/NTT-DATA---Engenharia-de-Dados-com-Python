# Contatos é o dicionário principal.
# "guilherme@gmail.com" e os demais são dicionários aninhados ao mesmo tempo que são a chave do dicionário principal.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# A criação da variável "telefone_giovanna" é opcional, pois podemos declarar diretamente no print(), mas isso, é claro, se você quiser apenas imprimir.
telefone_giovanna = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone_giovanna)
print(contatos["guilherme@gmail.com"])
