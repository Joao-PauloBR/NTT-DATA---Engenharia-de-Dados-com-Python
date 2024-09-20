print('''
        Olá, seja bem-vindo a caixa digitadora da NTT DATA!
    Todo o sistema foi remodelado para se adequar as necessidades do mercado. Espero que goste!
    Qualquer contratempo que tiver, não hesite em chamar um funcionário responsável e contate o suporte
    para que possamos corrigir o problema o mais rápido possível!
                                                    Desde já, agradecemos.
                                                                     att. NTT DATA.
''')

saldo = 1500
numero_saques = 0
lista_de_saques = []
lista_de_depositos = []

def depositar():
    global saldo
    global lista_de_depositos
    deposito = float(input("Digite o valor do depósito: "))
    if deposito >= 0.01:
        saldo += deposito
        print(f"Depósito realizado com sucesso. O valor de R$ {deposito:.2f} foi transferido.")
        print(f"Seu saldo atual é R$ {saldo:.2f}")
        lista_de_depositos.append(deposito)
    elif deposito <= 0:
        print(f"Você não pode depositar R$ {deposito:.2f}. Insira um valor válido.")
    else:
        print("Erro de sistema. Tente novamente mais tarde.")

def sacar():
    global saldo
    global numero_saques
    global lista_de_saques
    if numero_saques < 3:
        saque = float(input("Digite o valor que deseja sacar: "))
        if saque <= saldo and saque >= 0.01:
            if saque <= 500:
                saldo -= saque
                print(f"Saque efetuado com sucesso. Você sacou R$ {saque:.2f}. Seu saldo atual é de R$ {saldo:.2f}")
                lista_de_saques.append(saque)
                numero_saques += 1
            elif saque > 500:
                print("Você possui saldo suficiente, porém não podemos permitir saques maiores do que R$ 500.00")
        elif saque > saldo:
            print(f"ERRO! Você está tentando sacar um valor maior do que possui de saldo. Seu saldo atual é R$ {saldo:.2f}")
        else:
            print(f"Você não pode sacar R$ {saque:.2f}. Insira um valor válido.")
    else:
        print("Você já realizou três saques hoje. Por segurança, volte amanhã se deseja sacar novamente.")

def imprimir_extrato():
    global saldo
    global lista_de_depositos
    global lista_de_saques

    print("Depósitos realizados na sua conta")
    for deposito in lista_de_depositos:
        print(f"R$ {deposito:.2f}")

    print("==============================")

    print("Saques realizados na sua conta")
    for saque in lista_de_saques:
        print(f"R$ {saque:.2f}")

    print("==============================")
    print(f"Saldo atual da sua conta: R$ {saldo:.2f}")

while(True):
    try:
        print('''      
            =========== MENU ===========      
            
            [1] - Depósito
            [2] - Extrato
            [3] - Saque
            [0] - Sair
            
            ============================  
        ''')
        opcao = int(input("Escolha uma das opções: "))
        if opcao == 1:
            depositar()

        elif opcao == 2:
            imprimir_extrato()
        
        elif opcao == 3:
            sacar()

        elif opcao == 0:
            break
        
        else:
            print("Número inválido. Digite uma das opções mostradas no MENU.")

    except ValueError:
     # Mensagem de erro se o usuário digitar algo que não seja um número inteiro
        print("Entrada inválida. Por favor, digite um número inteiro.")