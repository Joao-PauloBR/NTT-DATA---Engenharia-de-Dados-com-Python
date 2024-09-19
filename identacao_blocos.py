def sacar(valor: float):
    saldo = 500.25
    if saldo >= valor:
        print("valor sacado.")
    else:
        print(f"Saldo insuficiente. Você possui R${saldo} na sua conta.")
    print("Obrigado por utilizar os nossos serviços. Volte sempre!")

sacar(100)
sacar(1200)