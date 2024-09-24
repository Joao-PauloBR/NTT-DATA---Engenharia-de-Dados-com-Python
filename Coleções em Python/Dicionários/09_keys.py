# O método .keys() serve para mostrar todas as chaves presentes em um dicionário. Mas

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
            "joao@gmail.com":{"nome": "João", "telefone": "3383-3324"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

# Se eu quiser saber quais são as chaves dentro de um dicionário aninhado, siga as etapas abaixo:
dados_guilherme = contatos["guilherme@gmail.com"]

# Obtendo as chaves do dicionário aninhado
chaves_dados_guilherme = dados_guilherme.keys()

print(chaves_dados_guilherme)  # dict_keys(['nome', 'telefone'])