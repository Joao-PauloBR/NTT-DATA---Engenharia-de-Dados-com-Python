# O método values() retorna uma visão (ou "view") de todos os valores contidos no dicionário.
# Ele é útil quando você deseja acessar ou iterar sobre os valores, sem se preocupar com as chaves.

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(contatos.values())

print("=" * 50)

celular = {"Modelo": "Moto G73", "Marca": "Motorola", "Ano": "2021", "Sistema Operacional": "Android 14"}
print(celular.values())

