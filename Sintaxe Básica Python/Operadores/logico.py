# AND = para ser TRUE tudo tem que ser TRUE
# OR = para ser TRUE apenas um tem que ser TRUE


# AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

######################

## OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#####################

saldo = 300
saque = 100
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp)

# Seguindo as boas práticas, é recomendado sempre quebrar grandes expressões em expressões menores
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo>= saque
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)