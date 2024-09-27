from datetime import datetime

print('''
            Olá, seja bem-vindo a caixa digitadora da NTT DATA!
        Todo o sistema foi remodelado para se adequar as necessidades do mercado. Espero que goste!
        Qualquer contratempo que tiver, não hesite em chamar um funcionário responsável e contate o suporte
        para que possamos corrigir o problema o mais rápido possível!
                                                        Desde já, agradecemos.
                                                                att. NTT DATA.
''')

# Variáveis existentes para transações financeiras
mascara_ptbr = "%d/%m/%Y %H:%M"
quantidade_transacao = 10

# Novas listas para a versão 3.0
usuarios = []  # Lista de usuários
contas = []  # Lista de contas
numero_conta_sequencial = 1  # Controle para o número da conta

# Funções para a versão 3.0

def cadastrar_usuario():
    global usuarios
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    cpf = input("Digite o CPF (somente números): ")
    endereco = input("Digite o endereço (logradouro, número - Bairro - Cidade/Estado): ")
    
    # Verificar se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário cadastrado com este CPF.")
            return
    
    # Criar e adicionar o novo usuário
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta():
    global contas, numero_conta_sequencial
    cpf = input("Digite o CPF do usuário para vincular a conta: ")

    # Verificar se o usuário existe
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        conta = {
            "agencia": "0001",
            "numero_conta": numero_conta_sequencial,
            "usuario": usuario_encontrado,
            "saldo": 0.0,
            "numero_saques": 0,
            "numero_depositos": 0,
            "lista_de_saques": [],
            "lista_de_depositos": [],
            "data_hora_saque": [],
            "data_hora_deposito": []
        }
        contas.append(conta)
        numero_conta_sequencial += 1
        print(f"Conta número {conta['numero_conta']} criada com sucesso para o usuário {usuario_encontrado['nome']}!")
    else:
        print("Erro: Usuário não encontrado. Cadastre o usuário primeiro.")

def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}")

def listar_contas():
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        print("Contas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")

def buscar_conta_por_usuario():
    cpf = input("Digite o CPF do usuário: ")

    # Verificar se o usuário existe
    conta_encontrada = None
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        return conta_encontrada
    else:
        print("Erro: Conta não encontrada.")
        return None

# Modificação da função que controla as transações para verificar se há usuários e contas cadastrados
def verificar_usuarios_e_contas():
    if len(usuarios) == 0 or len(contas) == 0:
        print("Erro: Para realizar transações, é necessário ter pelo menos um usuário e uma conta cadastrados.")
        return False
    return True

def depositar():
    if not verificar_usuarios_e_contas():
        return
    
    conta = buscar_conta_por_usuario()
    if conta:
        if conta["numero_saques"] + conta["numero_depositos"] < 10:
            deposito = float(input("Digite o valor do depósito: "))
            if deposito >= 0.01:
                conta["saldo"] += deposito
                print(f"Depósito realizado com sucesso. O valor de R$ {deposito:.2f} foi transferido.")
                print(f"Seu saldo atual é R$ {conta['saldo']:.2f}")
                conta["lista_de_depositos"].append(deposito)
                conta["data_hora_deposito"].append(datetime.today())
                conta["numero_depositos"] += 1
            else:
                print(f"Você não pode depositar R$ {deposito:.2f}. Insira um valor válido.")
        else:
            print("Você excedeu o número de transações permitidas. Volte amanhã para realizar mais operações.")

def sacar():
    if not verificar_usuarios_e_contas():
        return
    
    conta = buscar_conta_por_usuario()
    if conta:
        if conta["numero_saques"] + conta["numero_depositos"] < 10:    
            if conta["numero_saques"] < 3:
                saque = float(input("Digite o valor que deseja sacar: "))
                if saque <= conta["saldo"] and saque >= 0.01:
                    if saque <= 500:
                        conta["saldo"] -= saque
                        print(f"Saque efetuado com sucesso. Você sacou R$ {saque:.2f}. Seu saldo atual é de R$ {conta['saldo']:.2f}")
                        conta["lista_de_saques"].append(saque)
                        conta["data_hora_saque"].append(datetime.today())
                        conta["numero_saques"] += 1
                    else:
                        print("Você possui saldo suficiente, porém não podemos permitir saques maiores do que R$ 500.00")
                elif saque > conta["saldo"]:
                    print(f"ERRO! Você está tentando sacar um valor maior do que possui de saldo. Seu saldo atual é R$ {conta['saldo']:.2f}")
                else:
                    print(f"Você não pode sacar R$ {saque:.2f}. Insira um valor válido.")
            else:
                print("Você já realizou três saques hoje. Por segurança, volte amanhã se deseja sacar novamente.")
        else:
            print("Você excedeu o número de transações permitidas. Volte amanhã para realizar mais operações.")

def imprimir_extrato():
    if not verificar_usuarios_e_contas():
        return
    
    conta = buscar_conta_por_usuario()
    if conta:
        # DEPÓSITOS
        if len(conta["lista_de_depositos"]) == 0:
            print("Não há depósitos realizados.")
        else:
            print("Depósitos realizados na sua conta")

        for data, deposito in zip(conta["data_hora_deposito"], conta["lista_de_depositos"]):
            data_formatada = data.strftime(mascara_ptbr)
            print(f'''
{data_formatada}
R$ {deposito:.2f}''')
        
        print("=" * 30)

        # SAQUES
        if len(conta["lista_de_saques"]) == 0:
            print("Não há saques realizados.")
        else:    
            print("Saques realizados na sua conta")

        for data, saque in zip(conta["data_hora_saque"], conta["lista_de_saques"]):
            data_formatada = data.strftime(mascara_ptbr)
            print(f'''
{data_formatada}
R$ {saque:.2f}''')

        print("=" * 30)

        print(f"Saldo atual da sua conta: R$ {conta['saldo']:.2f}")


# Adicionar as novas opções no menu
def menu():
    while(True):
        try:
            print('''      
                =========== MENU ===========      
                
                [1] - Depósito
                [2] - Extrato
                [3] - Saque
                [4] - Cadastrar Usuário
                [5] - Cadastrar Conta
                [6] - Listar Usuários
                [7] - Listar Contas
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

            elif opcao == 4:
                cadastrar_usuario()

            elif opcao == 5:
                cadastrar_conta()

            elif opcao == 6:
                listar_usuarios()

            elif opcao == 7:
                listar_contas()

            elif opcao == 0:
                break

            else:
                print("Número inválido. Digite uma das opções mostradas no MENU.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

menu()
