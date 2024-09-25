from datetime import datetime

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
numero_depositos = 0
lista_de_saques = []
lista_de_depositos = []
data_hora_saque = []
data_hora_deposito = []                 # contador_transação == 10 | contador_deposito + contador_saque = contador_transação não permita mais transações
mascara_ptbr = "%d/%m/%Y %H:%M"
quantidade_transacao = 10

def depositar():
    global saldo
    global lista_de_depositos
    global quantidade_transacao
    global numero_saques
    global numero_depositos
    if numero_saques + numero_depositos < 10:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito >= 0.01:
            saldo += deposito
            print(f"Depósito realizado com sucesso. O valor de R$ {deposito:.2f} foi transferido.")
            print(f"Seu saldo atual é R$ {saldo:.2f}")
            lista_de_depositos.append(deposito)
            data_hora_deposito.append(datetime.today())
            numero_depositos += 1
        elif deposito <= 0:
            print(f"Você não pode depositar R$ {deposito:.2f}. Insira um valor válido.")
        else:
            print("Erro de sistema. Tente novamente mais tarde.")
    else:
        print("Você excedeu o número de transações permitidas. Volte amanhã para realizar mais operações.")

def sacar():
    global saldo
    global numero_saques
    global lista_de_saques
    global numero_depositos
    if numero_saques + numero_depositos < 10:    
        if numero_saques < 3:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= saldo and saque >= 0.01:
                if saque <= 500:
                    saldo -= saque
                    print(f"Saque efetuado com sucesso. Você sacou R$ {saque:.2f}. Seu saldo atual é de R$ {saldo:.2f}")
                    lista_de_saques.append(saque)
                    data_hora_saque.append(datetime.today())
                    numero_saques += 1
                elif saque > 500:
                    print("Você possui saldo suficiente, porém não podemos permitir saques maiores do que R$ 500.00")
            elif saque > saldo:
                print(f"ERRO! Você está tentando sacar um valor maior do que possui de saldo. Seu saldo atual é R$ {saldo:.2f}")
            else:
                print(f"Você não pode sacar R$ {saque:.2f}. Insira um valor válido.")
        else:
            print("Você já realizou três saques hoje. Por segurança, volte amanhã se deseja sacar novamente.")
    else:
        print("Você excedeu o número de transações permitidas. Volte amanhã para realizar mais operações.")

def imprimir_extrato():
    global saldo
    global lista_de_depositos
    global lista_de_saques
    global data_hora_saque
    global data_hora_deposito
    global mascara_ptbr

    # DEPÓSITOS
    if len(lista_de_depositos) == 0:
        print("Não há depósitos realizados.")
    else:
        print("Depósitos realizados na sua conta")

    for data, deposito in zip(data_hora_deposito, lista_de_depositos):
        data_formatada = data.strftime(mascara_ptbr)
        print(f'''
{data_formatada}
R$ {deposito:.2f}''')
        
    print("=" * 30)

    # SAQUES
    if len(lista_de_saques) == 0:
        print("Não há saques realizados.")
    else:    
        print("Saques realizados na sua conta")

    for data, saque in zip(data_hora_saque, lista_de_saques):
        data_formatada = data.strftime(mascara_ptbr)
        print(f'''
{data_formatada}
R$ {saque:.2f}''')

    print("=" * 30)

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