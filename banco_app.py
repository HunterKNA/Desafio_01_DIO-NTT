usuarios = []

def registrar(username, nome, cpf, email, senha):
    if any(u["username"] == username for u in usuarios):
        print("Esse username já está em uso!")
        return

    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Certifique-se de que possui 11 números.")
        return

    if len(senha) < 8:
        print("Sua senha está curta demais! Deve conter no mínimo 8 dígitos.")
        return

    cadastro = {
        "username": username,
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "senha": senha
    }
    usuarios.append(cadastro)
    print(f"Cadastro confirmado, {username}!")

def login(username, senha):
    for u in usuarios:
        if u["username"] == username and u["senha"] == senha:
            print(f"Login bem-sucedido. Bem-vindo, {username}!")
            return True
    print("Usuário ou senha incorretos.")
    return False

menu = """
[r] Registrar
[l] Login
[0] Sair

=> """

menu_logado = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Logout

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
logado = False


while True:
    if not logado:
        opcao = input(menu)

        match opcao:
            case "r":
                username = input("Insira seu username: ")
                nome = input("Insira seu nome: ")
                cpf = input("Insira seu CPF sem pontuação: ")
                email = input("Insira seu e-mail: ")
                senha = input("Crie sua senha, deve conter no mínimo 8 dígitos: ")
                registrar(username, nome, cpf, email, senha)

            case "l":
                username = input("Insira seu username: ")
                senha = input("Insira sua senha: ")
                logado = login(username, senha)

            case "0":
                break

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
    else:
        opcao = input(menu_logado)

        match opcao:
            case "1":
                valor = float(input("Informe o valor do depósito: "))

                if valor > 0:
                    saldo += valor
                    extrato += f"Depósito: R$ {valor:.2f}\n"
                    print(f"Você depositou: R$ {valor:.2f}")
                else:
                    print("Operação falhou! O valor informado é inválido.")

            case "2":
                valor = float(input("Informe o valor do saque: "))

                excedeu_saldo = valor > saldo
                excedeu_limite = valor > limite
                excedeu_saques = numero_saques >= LIMITE_SAQUES

                if excedeu_saldo:
                    print(f"Operação falhou! Você não tem saldo suficiente. \nSeu saldo atual é de: R$ {saldo:.2f}")
                elif excedeu_limite:
                    print(f"Operação falhou! O valor do saque excede o limite. \nSeu limite atual para saque é de: R$ {limite:.2f}")
                elif excedeu_saques:
                    print(f"Operação falhou! Número máximo de saques excedido. \nO máximo de saques permitidos é de: {LIMITE_SAQUES}")
                elif valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    print(f"Você sacou: R$ {valor:.2f}")
                else:
                    print("Operação falhou! O valor informado é inválido.")

            case "3":
                print("\n================ EXTRATO ================")
                print("Não foram realizadas movimentações." if not extrato else extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("==========================================")

            case "0":
                logado = False
                print("Você foi desconectado.")

            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")