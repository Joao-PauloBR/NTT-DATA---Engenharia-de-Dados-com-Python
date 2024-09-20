conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

status = "Sucesso" if saldo >= saque else "Falha" # Operador ternário

print(status)


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconheceu o tipo de conta, entre em contato com o seu gerente.")

