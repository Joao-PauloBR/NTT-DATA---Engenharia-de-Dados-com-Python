# Criando um dicionário chamado pessoa usando a sintaxe de chaves ({}).
# O dicionário contém duas chaves: "nome" e "idade", com seus respectivos valores "João" e 20
pessoa = {"nome": "João", "idade": 20}
print(pessoa)

# Neste caso, você está criando o mesmo dicionário, mas usando a função dict().
# Essa função permite passar pares de chave-valor como argumentos nomeados. O resultado é o mesmo dicionário que o anterior
pessoa = dict(nome="João", idade=20)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "João", "idade": 20, "telefone": "3333-1234"}
print(pessoa)

print("================================")

celular = {"Modelo": "Moto G73", "Marca": "Motorola", "Ano": "2021", "Sistema Operacional": "Android 14"}
print(celular)
# Existem duas formas para criar dicionários:
# 1ª é o modelo acima, utilizando chaves
# 2ª é o modelo abaixo, utilizando a função dict()
# OBS: A função dict() não aceita espaços nos nomes dos argumentos, por isso, sou obrigado a utilizar o "_"
celular = dict(Modelo="Moto G73", Marca="Motorola", Ano="2021", Sistema_Operacional="Android 14")
print(celular)

# Só aceita um por vez. Caso queira adicionar vários, veja o método update()
celular["Leitor de Digitais"] = True
print(celular)