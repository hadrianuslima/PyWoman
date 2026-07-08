def CRUD_vendas():
    import pickle
    from validacoes import validar_cpf , validar_data , verificar_preco , verificar_letras , verificar_numeros , limpar_terminal
    from recup_dados import recuperar_clientes,recuperar_produtos,recuperar_vendas

    def gravar_vendas(vendas_loja):
        arq_vendas = open("vendas.dat", "wb")
        pickle.dump(vendas_loja, arq_vendas)
        arq_vendas.close()

    rosa_inicio = "\033[1;31;45m"
    rosa_final = "\033[m"
    vendas = recuperar_vendas()
    produtos = recuperar_produtos()
    clientes = recuperar_clientes()
    
    modulo = "3"
    while modulo == "3":
        limpar_terminal()
        print(rosa_inicio+"------------------------------------"+rosa_final)
        print(rosa_inicio+"|          MÓDULO DE VENDAS        |"+rosa_final)
        print(rosa_inicio+"------------------------------------"+rosa_final)
        print("|| 1- Adicionar venda✅           ||")
        print("|| 2- Visualizar vendasℹ️          ||")
        print("|| 3- Editar venda🔁              ||")
        print("|| 4- Excluir uma venda🗑️          ||")
        print("||  0- Voltar🔙                    /")
        print("  ---------------------------------")
        resp6 = input("Informe a opção desejada: ").strip()
        resp6_validas = ["0", "1", "2", "3", "4"]
        while not (resp6 in resp6_validas):
            resp6 = input("Informe uma opção válida: ").strip()
        if resp6 == "1":
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|          ADICIONAR VENDA         |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print("|| 1- Adicionar uma nova venda✅  ||")
            print("|| 2- Reativar uma venda🔁        ||")
            print("--------------------------------------")
            opcao = input("Informe a opção desejada: ").strip()
            while opcao != "1" and opcao != "2":
                opcao = input("Informe a opção desejada: ").strip()
            if opcao == "1":
                limpar_terminal()
                print(rosa_inicio+"------------------------------------"+rosa_final)
                print(rosa_inicio+"|             NOVA VENDA           |"+rosa_final)
                print(rosa_inicio+"------------------------------------"+rosa_final)
                id_venda = int(next(reversed(vendas))) + 1
                cpf_cliente = input("Informe o CPF de quem comprou o(s) produto(s): ").strip()
                while validar_cpf(cpf_cliente) == False:
                    cpf_cliente = input("Informe um CPF válido: ").strip()
                cpf_cliente = cpf_cliente.replace('.', '')
                cpf_cliente = cpf_cliente.replace('-', '')
                cpf_cliente = cpf_cliente.replace(' ', '')
                if cpf_cliente in clientes:
                    nome = clientes[cpf_cliente][0]
                    dia_da_compra = input("Informe a data da compra no formato DD/MM/AAAA: ").strip()
                    while validar_data(dia_da_compra) == False:
                        dia_da_compra = input("Informe a data correta no formato DD/MM/AAAA: ").strip()
                    codigo = input("Informe o código do produto: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    achou = ""
                    for setor in produtos:
                        if codigo in produtos[setor]:
                            achou = "S"
                            categoria = setor
                            break
                    if achou == "S":
                        preco = 0
                        quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                        while verificar_numeros(quantidade) == False:
                            quantidade = input("APENAS NÚMEROS: ").strip()
                        quantidade = int(quantidade)
                        if categoria == "roupas":
                            index_preco = 4
                        else:
                            index_preco = 2
                        preco += produtos[categoria][codigo][index_preco] * quantidade
                        vendas[str(id_venda)] = [
                            nome,
                            cpf_cliente,
                            dia_da_compra,
                            {codigo: quantidade},
                            preco,
                            True
                        ]
                        parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                        while parar != "N":
                            codigo = input("Informe o código do produto: ").strip()
                            while verificar_numeros(codigo) == False:
                                codigo = input("APENAS NÚMEROS: ").strip()
                            achou = ""
                            for setor in produtos:
                                if codigo in produtos[setor]:
                                    achou = "S"
                                    categoria = setor
                                    break
                            if achou == "S":
                                quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                                while verificar_numeros(quantidade) == False:
                                    quantidade = input("APENAS NÚMEROS: ").strip()
                                quantidade = int(quantidade)
                                if categoria == "roupas":
                                    index_preco = 4
                                else:
                                    index_preco = 2
                                preco += produtos[categoria][codigo][index_preco] * quantidade
                                vendas[id_venda][3][codigo] = quantidade
                                vendas[id_venda][4] = preco
                                parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                            else:
                                print("Esse produto não existe na loja!")
                                parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                        print(f"PREÇO TOTAL: R${preco}")
                        print()
                        print("--------------------------------")
                        print("|       VENDA CADASTRADA✅    |")
                        print("--------------------------------")
                        print()
                    else:
                        print("Esse produto não existe na loja!")
                else:
                    print("Esse cliente não está cadastrado no loja!")
                    print("Por favor realize o cadastro do cliente primeiro!")
            else:
                limpar_terminal()
                print(rosa_inicio+"------------------------------------"+rosa_final)
                print(rosa_inicio+"|          REATIVAR VENDA          |"+rosa_final)
                print(rosa_inicio+"------------------------------------"+rosa_final)
                achou = ""
                for id_venda in vendas:
                    if vendas[id_venda][5] == False:
                        achou = "S"
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"NOME: {vendas[id_venda][0]}")
                        print(f"DATA DA VENDA: {vendas[id_venda][2]}")
                        print(f"ID DA VENDA: {id_venda}")
                        print("\033[1;32m----------------------------------\033[m")
                if achou != "S":
                    print("Nenhuma venda desativada!")
                else:
                    reativacao = input("Informe o ID da venda que deseja reativar: ").strip()
                    while verificar_numeros(reativacao) == False:
                        reativacao = input("Informe o ID de forma correta: ").strip()
                    if reativacao in vendas and vendas[reativacao][5] == False:
                        vendas[reativacao][5] = True
                        print("--------------------------------")
                        print("|       VENDA CADASTRADA✅    |")
                        print("--------------------------------")
                    else:
                        print("O ID foi informado errado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp6 == "2":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|      VISUALIZAR VENDAS       |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            busca = input("Busque a venda pelo o nome do cliente: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
            achou = ""
            for id in vendas:
                if busca in vendas[id][0].lower() and vendas[id][5] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"NOME: {vendas[id][0]}")
                    print(f"DATA DA VENDA: {vendas[id][2]}")
                    print(f"ID DA VENDA: {id}")
                    print("\033[1;32m----------------------------------\033[m")
                    achou = "S"
            if achou != "S":
                print("Venda não encontrada!")
            else:
                id_venda = input("Informe o ID da venda que deseja visualizar: ").strip()
                while verificar_numeros(id_venda) == False:
                    id_venda = input("APENAS NÚMEROS: ").strip()
                if id_venda in vendas:
                    print()
                    print(f"NOME: {vendas[id_venda][0]}")
                    print(f"CPF: {vendas[id_venda][1]}")
                    print(f"DATA: {vendas[id_venda][2]}")
                    print("PRODUTOS E QUANTIDADES:")
                    for i in vendas[id_venda][3]:
                        print("-", end=" ")
                        print(f"{i}: {vendas[id_venda][3][i]}")
                    print(f"PREÇO TOTAL: R${vendas[id_venda][4]}")
                else:
                    print("Essa venda não está cadastrada!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp6 == "3":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|        EDITAR VENDA          |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            busca = input("Busque a venda pelo o nome do cliente: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
            achou = ""
            for id in vendas:
                if busca in vendas[id][0].lower() and vendas[id][5] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"NOME: {vendas[id][0]}")
                    print(f"DATA DA VENDA: {vendas[id][2]}")
                    print(f"ID DA VENDA: {id}")
                    print("\033[1;32m----------------------------------\033[m")
                    achou = "S"
            if achou != "S":
                print("Venda não encontrada!")
            else:
                id_venda = input("Informe o ID da venda que deseja editar: ").strip()
                while verificar_numeros(id_venda) == False:
                    id_venda = input("APENAS NÚMEROS: ").strip()
                if id_venda in vendas:
                    print()
                    print(f"NOME: {vendas[id_venda][0]}")
                    print(f"CPF: {vendas[id_venda][1]}")
                    print(f"DATA: {vendas[id_venda][2]}")
                    print("PRODUTOS E QUANTIDADES:")
                    for i in vendas[id_venda][3]:
                        print("-", end=" ")
                        print(f"{i}: {vendas[id_venda][3][i]}")
                    print(f"PREÇO TOTAL: R${vendas[id_venda][4]}")
                    print()
                    preco = 0
                    dia_da_compra = input("Informe a data  CORRETA da compra no formato DD/MM/AAAA: ").strip()
                    while validar_data(dia_da_compra) == False:
                        dia_da_compra = input("Informe a data correta no formato DD/MM/AAAA: ").strip()
                    codigo = input("Informe o código CORRETO do produto: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    achou = ""
                    for setor in produtos:
                        if codigo in produtos[setor]:
                            achou = "S"
                            categoria = setor
                            break
                    if achou == "S":
                        quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                        while verificar_numeros(quantidade) == False:
                            quantidade = input("APENAS NÚMEROS: ").strip()
                        quantidade = int(quantidade)
                        if categoria == "roupas":
                            index_preco = 4
                        else:
                            index_preco = 2
                        preco += produtos[categoria][codigo][index_preco] * quantidade
                        vendas[id_venda] = [
                            vendas[id_venda][0],
                            vendas[id_venda][1],
                            dia_da_compra,
                            {codigo: quantidade},
                            preco,
                            True
                        ]
                        parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                        while parar != "N":
                            codigo = input("Informe o código do produto: ").strip()
                            while verificar_numeros(codigo) == False:
                                codigo = input("APENAS NÚMEROS: ").strip()
                            achou = ""
                            for setor in produtos:
                                if codigo in produtos[setor]:
                                    achou = "S"
                                    categoria = setor
                                    break
                            if achou == "S":
                                quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                                while verificar_numeros(quantidade) == False:
                                    quantidade = input("APENAS NÚMEROS: ").strip()
                                quantidade = int(quantidade)
                                if categoria == "roupas":
                                    index_preco = 4
                                else:
                                    index_preco = 2
                                preco += produtos[categoria][codigo][index_preco] * quantidade
                                vendas[id_venda][3][codigo] = int(quantidade)
                                vendas[id_venda][4] = preco
                                parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                            else:
                                print("Produto não encontrado!")
                                parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                        print()
                        print("--------------------------------")
                        print("|        VENDA EDITADA✅      |")
                        print("--------------------------------")
                        print()
                    else:
                        print("Produto não encontrado!")
                else:
                    print("Esse ID não está cadastrado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp6 == "4":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|         EXCLUIR VENDA        |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print()
            busca = input("Busque pelo nome do cliente: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
            achou = ""
            for id in vendas:
                if busca in vendas[id][0].lower() and vendas[id][5] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"NOME: {vendas[id][0]}")
                    print(f"DATA DA VENDA: {vendas[id][2]}")
                    print(f"ID DA VENDA: {id}")
                    print("\033[1;32m----------------------------------\033[m")
                    achou = "S"
            if achou != "S":
                print("Venda não encontrada!")
            else:
                id_venda = input("Informe o ID da venda que deseja excluir: ").strip()
                while verificar_numeros(id_venda) == False:
                    id_venda = input("APENAS NÚMEROS: ").strip()
                if id_venda in vendas:
                    print()
                    print(f"NOME: {vendas[id_venda][0]}")
                    print(f"CPF: {vendas[id_venda][1]}")
                    print(f"DATA: {vendas[id_venda][2]}")
                    print("PRODUTOS E QUANTIDADES:")
                    for i in vendas[id_venda][3]:
                        print("-", end=" ")
                        print(f"{i}: {vendas[id_venda][3][i]}")
                    print(f"PREÇO TOTAL: R${vendas[id_venda][4]}")
                    excluir = input("Digite S para confirmar a exclusão: ").strip().upper()
                    if excluir == "S":
                        vendas[id_venda][5] = False
                        print()
                        print("--------------------------------")
                        print("|        VENDA EXCLUÍDA✅      |")
                        print("--------------------------------")
                        print()
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Essa venda não está cadastrada!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        else:
            gravar_vendas(vendas)
            break