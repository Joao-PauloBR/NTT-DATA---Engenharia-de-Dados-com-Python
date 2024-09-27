from datetime import datetime, date

print('''
            Olá, seja bem-vindo ao sistema bancário da NTT DATA!
        Todo o sistema foi remodelado para se adequar as necessidades do mercado. Espero que goste!
        Qualquer contratempo que tiver, não hesite em chamar um funcionário responsável e contate o suporte
        para que possamos corrigir o problema o mais rápido possível!
                                                        Desde já, agradecemos.
                                                                att. NTT DATA.
''')

MASCARA_DATA_HORA_PTBR = "%d/%m/%Y %H:%M"
MASCARA_DATA_PTBR = "%d/%m/%Y"
QUANTIDADE_TRANSACAO = 10

usuarios = []  # Lista de usuários
contas = []  # Lista de contas
numero_conta_sequencial = 1  # Controle para o número da conta
usuario_atual = None  # Variável para armazenar o usuário atualmente logado
conta_atual = None  # Variável para armazenar a conta corrente selecionada

def cadastrar_usuario():
    global usuarios
    nome = input("Digite o nome do usuário: ")
    
    while True:
        data_nascimento_str = input("Digite a data de nascimento (dd/mm/yyyy): ")
        try:
            data_nascimento = datetime.strptime(data_nascimento_str, MASCARA_DATA_PTBR).date()
            break
        except ValueError:
            print("Erro: Data no formato inválido. Por favor, use o formato dd/mm/yyyy.")
    
    cpf = input("Digite o CPF (somente números): ")
    endereco = input("Digite o endereço (logradouro, número - Bairro - Cidade/Estado): ")
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário cadastrado com este CPF.")
            return
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def deletar_usuario():
    cpf = input("Digite o CPF do usuário que deseja deletar: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        contas_vinculadas = [conta for conta in contas if conta['usuario'] == usuario_encontrado]
        if len(contas_vinculadas) > 0:
            print(f"Erro: O usuário ainda tem {len(contas_vinculadas)} conta(s) vinculada(s). Delete todas as contas antes de excluir o usuário.")
        else:
            usuarios.remove(usuario_encontrado)
            print(f"Usuário {usuario_encontrado['nome']} deletado com sucesso!")
    else:
        print("Erro: Usuário com este CPF não encontrado.")

def editar_usuario():
    cpf = input("Digite o CPF do usuário que deseja editar: ")
    
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        print(f"Editando informações do usuário {usuario_encontrado['nome']}")
        
        novo_nome = input(f"Novo nome ({usuario_encontrado['nome']}): ") or usuario_encontrado['nome']
        
        while True:
            nova_data_nascimento_str = input(f"Nova data de nascimento ({usuario_encontrado['data_nascimento'].strftime(MASCARA_DATA_PTBR)}): ") or usuario_encontrado['data_nascimento'].strftime(MASCARA_DATA_PTBR)
            try:
                nova_data_nascimento = datetime.strptime(nova_data_nascimento_str, MASCARA_DATA_PTBR).date()
                break
            except ValueError:
                print("Erro: Data no formato inválido. Por favor, use o formato dd/mm/yyyy.")
        
        novo_endereco = input(f"Novo endereço ({usuario_encontrado['endereco']}): ") or usuario_encontrado['endereco']
        
        usuario_encontrado['nome'] = novo_nome
        usuario_encontrado['data_nascimento'] = nova_data_nascimento
        usuario_encontrado['endereco'] = novo_endereco
        
        print("Informações atualizadas com sucesso!")
    else:
        print("Erro: Usuário com este CPF não encontrado.")

def cadastrar_conta():
    global contas, numero_conta_sequencial
    cpf = input("Digite o CPF do usuário para vincular a conta: ")

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

def deletar_conta():
    numero_conta = int(input("Digite o número da conta que deseja deletar: "))

    conta_encontrada = None
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            conta_encontrada = conta
            break

    if conta_encontrada:
        contas.remove(conta_encontrada)
        print(f"Conta número {numero_conta} deletada com sucesso!")
    else:
        print("Erro: Conta com este número não encontrada.")

def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Data de Nascimento: {usuario['data_nascimento'].strftime(MASCARA_DATA_PTBR)}")
            print(f"Endereço: {usuario['endereco']}")
            print("=" * 30)

def listar_contas():
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
    else:
        print("Contas cadastradas:")
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}, CPF: {conta['usuario']['cpf']}")

def trocar_usuario():
    global usuario_atual, conta_atual
    cpf = input("Digite o CPF do usuário: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break
    
    if usuario_encontrado:
        usuario_atual = usuario_encontrado
        conta_atual = None
        print(f"Usuário {usuario_atual['nome']} selecionado com sucesso!")
    else:
        print("Erro: Usuário não encontrado.")

def trocar_conta_corrente():
    global conta_atual
    if usuario_atual is None:
        print("Erro: Nenhum usuário selecionado.")
        return
    
    contas_do_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == usuario_atual["cpf"]]
    
    if len(contas_do_usuario) == 0:
        print("Erro: Nenhuma conta encontrada para este usuário.")
        return

    print(f"Contas disponíveis para o usuário {usuario_atual['nome']}:")
    for conta in contas_do_usuario:
        print(f"Conta {conta['numero_conta']} - Agência {conta['agencia']}")

    numero_conta = int(input("Digite o número da conta que deseja selecionar: "))
    
    conta_encontrada = None
    for conta in contas_do_usuario:
        if conta["numero_conta"] == numero_conta:
            conta_encontrada = conta
            break
    
    if conta_encontrada:
        conta_atual = conta_encontrada
        print(f"Conta número {conta_atual['numero_conta']} selecionada com sucesso!")
    else:
        print("Erro: Conta não encontrada.")

def verificar_usuario_e_conta():
    if usuario_atual is None:
        print("Erro: Nenhum usuário selecionado.")
        return False
    if conta_atual is None:
        print("Erro: Nenhuma conta selecionada.")
        return False
    return True

def depositar():
    if not verificar_usuario_e_conta():
        return
    
    if conta_atual["numero_saques"] + conta_atual["numero_depositos"] < QUANTIDADE_TRANSACAO:
        deposito = float(input("Digite o valor do depósito: "))
        if deposito >= 0.01:
            conta_atual["saldo"] += deposito
            print(f"Depósito realizado com sucesso. O valor de R$ {deposito:.2f} foi transferido.")
            print(f"Seu saldo atual é R$ {conta_atual['saldo']:.2f}")
            conta_atual["lista_de_depositos"].append(deposito)
            conta_atual["data_hora_deposito"].append(datetime.today())
            conta_atual["numero_depositos"] += 1
        else:
            print(f"Você não pode depositar R$ {deposito:.2f}. Insira um valor válido.")
    else:
        print("Você excedeu o número de transações permitidas. Volte amanhã para realizar mais operações.")

def sacar():
    if not verificar_usuario_e_conta():
        return
    
    if conta_atual["numero_saques"] + conta_atual["numero_depositos"] < QUANTIDADE_TRANSACAO:    
        if conta_atual["numero_saques"] < 3:
            saque = float(input("Digite o valor que deseja sacar: "))
            if saque <= conta_atual["saldo"] and saque >= 0.01:
                if saque <= 500:
                    conta_atual["saldo"] -= saque
                    print(f"Saque efetuado com sucesso. Você sacou R$ {saque:.2f}. Seu saldo atual é de R$ {conta_atual['saldo']:.2f}")
                    conta_atual["lista_de_saques"].append(saque)
                    conta_atual["data_hora_saque"].append(datetime.today())
                    conta_atual["numero_saques"] += 1
                else:
                    print("Você possui saldo suficiente, porém não podemos permitir saques maiores do que R$ 500.00")
            elif saque > conta_atual["saldo"]:
                print(f"ERRO! Você está tentando sacar um valor maior do que possui de saldo. Seu saldo atual é R$ {conta_atual['saldo']:.2f}")
            else:
                print(f"Você não pode sacar R$ {saque:.2f}. Insira um valor válido.")
        else:
            print("Você já realizou três saques hoje. Por segurança, volte amanhã se deseja sacar novamente.")
    else:
        print("Você excedeu o número de transações permitidas. Volte amanhã para realizar mais operações.")

def imprimir_extrato():
    if not verificar_usuario_e_conta():
        return
    
    # DEPÓSITOS
    if len(conta_atual["lista_de_depositos"]) == 0:
        print("Não há depósitos realizados.")
    else:
        print("Depósitos realizados na sua conta")

    for data, deposito in zip(conta_atual["data_hora_deposito"], conta_atual["lista_de_depositos"]):
        data_formatada = data.strftime(MASCARA_DATA_HORA_PTBR)
        print(f'''
{data_formatada}
R$ {deposito:.2f}''')
    
    print("=" * 30)

    # SAQUES
    if len(conta_atual["lista_de_saques"]) == 0:
        print("Não há saques realizados.")
    else:    
        print("Saques realizados na sua conta")

    for data, saque in zip(conta_atual["data_hora_saque"], conta_atual["lista_de_saques"]):
        data_formatada = data.strftime(MASCARA_DATA_HORA_PTBR)
        print(f'''
{data_formatada}
R$ {saque:.2f}''')

    print("=" * 30)

    print(f"Saldo atual da sua conta: R$ {conta_atual['saldo']:.2f}")

def menu():
    etapa_atual = 1

    while True:
        while etapa_atual == 1:
            try:
                print('''      
        =========== 1ª ETAPA ===========      
        
        [1] - Cadastrar Usuário
        [2] - Deletar Usuário
        [3] - Editar Usuário
        [4] - Cadastrar Conta-Corrente
        [5] - Deletar Conta-Corrente
        [6] - Avançar
        [7] - Sair
        
        ================================
            ''')

                opcao = int(input("Escolha uma das opções: "))

                if opcao == 1:
                    cadastrar_usuario()
                elif opcao == 2:
                    if len(usuarios) == 0:
                        print("Nenhum usuário foi cadastrado para poder ser deletado.")
                    else:
                        deletar_usuario()
                elif opcao == 3:
                    if len(usuarios) == 0:
                        print("Nenhum usuário foi cadastrado para poder editado.")
                    else:
                        editar_usuario()
                elif opcao == 4:
                    cadastrar_conta()
                elif opcao == 5:
                    if len(contas) == 0:
                        print("Nenhuma conta cadastrada para deletar.")
                    else:
                        deletar_conta()
                elif opcao == 6:
                    if len(usuarios) == 0 and len(contas) == 0:
                        print("Erro: É necessário cadastrar pelo menos um usuário e uma conta-corrente para continuar.")
                    elif len(usuarios) > 0 and len(contas) == 0:
                        print("Erro: É necessário cadastrar pelo menos uma conta-corrente para continuar.")
                    else:
                        etapa_atual = 2
                elif opcao == 7:
                    print("Saindo...")
                    return
                else:
                    print("Número inválido. Digite uma das opções mostradas.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

        while etapa_atual == 2:
            try:
                print('''      
        =========== 2ª ETAPA ===========      
        
        [1] - Voltar
        [2] - Escolher Usuário
        [3] - Escolher Conta-Corrente
        [4] - Listar Usuários
        [5] - Listar Contas-Correntes
        [6] - Avançar
        [7] - Sair
        
        ================================
                ''')

                opcao = int(input("Escolha uma das opções: "))

                if opcao == 1:
                    etapa_atual = 1
                elif opcao == 2:
                    trocar_usuario()
                elif opcao == 3:
                    trocar_conta_corrente()
                elif opcao == 4:
                    listar_usuarios()
                elif opcao == 5:
                    listar_contas()
                elif opcao == 6:
                    if usuario_atual and conta_atual:
                        etapa_atual = 3
                    else:
                        print("Erro: Escolha um usuário e uma conta-corrente antes de avançar.")
                elif opcao == 7:
                    print("Saindo...")
                    return
                else:
                    print("Número inválido. Digite uma das opções mostradas.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

        while etapa_atual == 3:
            try:
                print('''      
        =========== 3ª ETAPA ===========      
        
        [1] - Voltar
        [2] - Depositar
        [3] - Sacar
        [4] - Extrato
        [5] - Sair
        
        ================================
                ''')

                opcao = int(input("Escolha uma das opções: "))

                if opcao == 1:
                    etapa_atual = 2
                elif opcao == 2:
                    depositar()
                elif opcao == 3:
                    sacar()
                elif opcao == 4:
                    imprimir_extrato()
                elif opcao == 5:
                    print("Saindo...")
                    return
                else:
                    print("Número inválido. Digite uma das opções mostradas.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

menu()
