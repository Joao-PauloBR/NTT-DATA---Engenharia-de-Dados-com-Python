nome = "João Paulo"
idade = 20
profissão = "Estudante, futuro programador"
linguagem = "Python"
saldo = 45.4354

dados = {"nome": "João Paulo", "idade": 20}

print("Nome: %s Idade: %d" % (nome, idade)) # OLD Style

print("Nome: {} Idade: {}".format (nome, idade))

print("Nome: {1} Idade: {0}".format (idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} Nome: {1}".format (idade, nome))

print("Nome: {name} Idade: {age}".format (age = idade, name = nome))
print("Nome: {nome} Idade: {idade}".format (**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")