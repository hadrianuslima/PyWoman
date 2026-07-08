def CRUD_cliente():
    import pickle
    from validacoes import validar_cpf , validar_data , verificar_letras , limpar_terminal, validar_fone
    from recup_dados import recuperar_clientes

    def gravar_clientes(clientes_loja):
        arq_clientes = open("clientes.dat", "wb")
        pickle.dump(clientes_loja, arq_clientes)
        arq_clientes.close()

    rosa_inicio = "\033[1;31;45m"
    rosa_final = "\033[m"
    clientes = recuperar_clientes()
    modulo = "1"
    while modulo == "1":
        limpar_terminal()
        print(rosa_inicio+"--------------------------------"+rosa_final)
        print(rosa_inicio+"|      MÓDULO DE CLIENTES      |"+rosa_final)
        print(rosa_inicio+"--------------------------------"+rosa_final)
        print("|| 1- Cadastrar cliente✅     ||")
        print("|| 2- Ver dados do clienteℹ️   ||")
        print("|| 3- Atualizar dados🔁       ||")
        print("|| 4- Excluir cadastro 🗑️      ||")
        print("||  0- Voltar🔙                /")
        print("  ----------------------------")
        resp1 = input("Informe a opção que deseja: ").strip()
        resp1_validas = ["0", "1", "2", "3", "4"]
        while not (resp1 in resp1_validas):
            resp1 = input("Informe uma opção válida: ").strip()
        if resp1 == "1":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|      CADASTRAR CLIENTE       |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print()
            cpf_cliente = input("Informe o CPF do cliente no formato XXX.XXX.XXX-XX: ").strip()
            while validar_cpf(cpf_cliente) == False:
                cpf_cliente = input("Informe um CPF válido: ").strip()
            cpf_cliente = cpf_cliente.replace('.', '')
            cpf_cliente = cpf_cliente.replace('-', '')
            cpf_cliente = cpf_cliente.replace(' ', '')
            if not (cpf_cliente in clientes):
                nome = input("Informe o nome do cliente: ").strip().capitalize()
                while verificar_letras(nome) == False:
                    nome = input("Informe o nome CORRETO do cliente : ").strip().capitalize()
                fone = input("Informe o número do telefone do cliente: ").strip()
                while validar_fone(fone) == False:
                    fone = input("Informe o número válido: ").strip()
                fone = fone.replace(" ","")
                fone = fone.replace("-","")
                fone = fone.replace("(","")
                fone = fone.replace(")","")
                data_nasc = input("Informe a data de nascimento do cliente no formato DD/MM/AAAA: ").strip()
                while validar_data(data_nasc) == False:
                    data_nasc = input("Informe a data válida no formato DD/MM/AAAA: ").strip()
                clientes[cpf_cliente] = [
                    nome,
                    fone,
                    cpf_cliente,
                    data_nasc,
                    True
                ]
                print()
                print("--------------------------------")
                print("|      CLIENTE CADASTRADO ✅   |")
                print("--------------------------------")
                print()
            elif (cpf_cliente in clientes) and clientes[cpf_cliente][4] == False:
                print("\033[1;32m----------------------------------\033[m")
                print(f"CPF: {clientes[cpf_cliente][2]}")
                print(f"NOME: {clientes[cpf_cliente][0]}")
                print(f"TELEFONE: {clientes[cpf_cliente][1]}")
                print(f"DATA DE NASCIMENTO: {clientes[cpf_cliente][3]}")
                print("\033[1;32m----------------------------------\033[m")
                reativacao = input("Deseja reativar o cadastro desse cliente? [S/N]: ").strip().upper()
                while verificar_letras(reativacao) == False:
                    reativacao = input("APENAS LETRAS! [S/N]: ").strip().upper()
                if reativacao == "S":
                    clientes[cpf_cliente][4] = True
                    print("--------------------------------")
                    print("|      CLIENTE CADASTRADO ✅   |")
                    print("--------------------------------")
                else:
                    print("Cadastro cancelado!")
            else:
                print("Esse CPF já está cadastrado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp1 == "2":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|       DADOS DO CLIENTES      |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print()
            busca = input("NOME: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
            achou = ""
            for i in clientes:
                if busca in clientes[i][0].lower() and clientes[i][4] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CPF: {clientes[i][2]}")
                    print(f"NOME: {clientes[i][0]}")
                    print(f"TELEFONE: {clientes[i][1]}")
                    print(f"DATA DE NASCIMENTO: {clientes[i][3]}")
                    print("\033[1;32m----------------------------------\033[m")
                    achou = "S"
            if (
                achou != "S"
            ):  # Usei como forma de informar se não há cliente relacionado a pesquisa
                print("Cliente não encontrado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp1 == "3":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|       ATUALIZAR DADOS        |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print()
            busca = input("NOME: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS: ").strip().lower()
            achou = ""
            for i in clientes:
                if busca in clientes[i][0].lower() and clientes[i][4] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CPF: {clientes[i][2]}")
                    print(f"NOME: {clientes[i][0]}")
                    print("\033[1;32m----------------------------------\033[m")
                    achou = "S"
            if (
                achou != "S"
            ):  # Usei como forma de informar se não há cliente relacionado a pesquisa
                print("Cliente não encontrado!")
            else:
                cpf_cliente = input("Informe o CPF do cliente que deseja editar: ").strip()
                while validar_cpf(cpf_cliente) == False:
                    cpf_cliente = input("Informe um CPF válido: ").strip()
                if cpf_cliente in clientes:
                    print(f"NOME: {clientes[cpf_cliente][0]}")
                    print(f"TELEFONE: {clientes[cpf_cliente][1]}")
                    print(f"DATA DE NASCIMENTO: {clientes[cpf_cliente][3]}")
                    nome = input("Informe o novo nome para o cliente: ").strip().capitalize()
                    while verificar_letras(nome) == False:
                        nome = input("Informe o nome CORRETO do cliente : ").strip().capitalize()
                    data_nasc = input("Informe a nova data de nascimento para cliente: ").strip()
                    while validar_data(data_nasc) == False:
                        data_nasc = input("Informe a data correta no formato DD/MM/AAAA: ").strip()
                    fone = input("Informe o novo número telefone cliente: ").strip()
                    while validar_fone(fone) == False:
                        fone = input("Informe um número válido: ").strip()
                    clientes[cpf_cliente][0] = nome
                    clientes[cpf_cliente][3] = data_nasc
                    clientes[cpf_cliente][1] = fone
                    print()
                    print("--------------------------------")
                    print("|      DADOS ATUALIZADOS✅     |")
                    print("--------------------------------")
                else:
                    print("Esse CPF não está cadastrado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp1 == "4":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|        EXCLUIR CADASTRO      |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print()
            busca = input("NOME: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
            achou = ""
            for i in clientes:
                if busca in clientes[i][0].lower() and clientes[i][4] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CPF: {clientes[i][2]}")
                    print(f"NOME: {clientes[i][0]}")
                    print("\033[1;32m----------------------------------\033[m")
                    achou = "S"
            if achou != "S":
                print("Cliente não encontrado!")
            else:
                cpf_cliente = input("Informe o CPF do cliente que deseja excluir: ").strip()
                while validar_cpf(cpf_cliente) == False:
                    cpf_cliente = input("Informe um CPF válido: ").strip()
                if cpf_cliente in clientes:
                    print(f"NOME: {clientes[cpf_cliente][0]}")
                    print(f"CPF: {clientes[cpf_cliente][2]}")
                    print(f"TELEFONE: {clientes[cpf_cliente][1]}")
                    print(f"DATA DE NASCIMENTO: {clientes[cpf_cliente][3]}")
                    excluir = input("Digite S para excluir o cadastro: ").strip().upper()
                    if excluir == "S":
                        clientes[cpf_cliente][4] = False
                        print("--------------------------------")
                        print("|       CADASTRO EXCLUÍDO✅    |")
                        print("--------------------------------")
                        print()
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Esse CPF não está cadastrado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        else:
            gravar_clientes(clientes)
            break     