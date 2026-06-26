def CRUD_vendas():
    import pickle
    from validacoes import validar_cpf , validar_data , verificar_preco , verificar_letras , verificar_numeros , limpar_terminal

    def recuperar_vendas():
        try:
            arq_vendas = open("vendas.dat", "rb")
            vendas = pickle.load(arq_vendas)
            arq_vendas.close()
        except:
            arq_vendas = open("vendas.dat", "wb")
            vendas = {  # Aqui nesse dicionário eu coloquei um ID para cada venda,
                # que recebe uma lista no qual tem o nome do cliente, CPF, data da venda,
                # um dicionário onde tem códigos do produto como chave e sua respectiva quantidade, o valor total da venda , e o status da venda
                "11111": [
                    "Hadrianus da silva lima",
                    "11111111111",
                    "11/11/2011",
                    {"123": 3, "234": 2},
                    1000.00,
                    True
                ],
                "22222": [
                    "Valeria pereira de medeiros",
                    "22222222222",
                    "11/11/2011",
                    {"123": 3, "234": 4},
                    1500.00,
                    True
                ],
                "33333": [
                    "Marycele saraiva da silva",
                    "33333333333",
                    "12/11/2011",
                    {"234": 6, "345": 9},
                    2000.00,
                    True
                ],
            }
            pickle.dump(vendas, arq_vendas)
            arq_vendas.close()
        return vendas
    def recuperar_produtos():
        try:
            arq_produtos = open("produtos.dat", "rb")
            produtos = pickle.load(arq_produtos)
            arq_produtos.close()
        except:
            arq_produtos = open("produtos.dat", "wb")
            produtos = {
                "roupas": {
                    "123": ["blusa", "M", "123", "preto", 50.00, True],
                    "234": ["vestido", "P", "234", "azul", 70.00, True],
                    "345": ["calça", "G", "345", "vermelho", 40.00, True],
                    "456": ["sutiã", "M", "456", "preto", 30.00, True],
                },
                "cosmeticos": {
                    "567": ["maquiagem", "567", 70.00, True],
                    "678": ["perfume", "678", 80.00, True],
                    "789": ["hidratante", "789", 65.00, True],
                    "890": ["óleo corporal", "890", 30.50, True],
                },
                "acessorios": {
                    "901": ["pulseira", "901", 38.90, True],
                    "012": ["colar", "012", 79.99, True],
                    "112": ["óculos", "112", 58.99, True],
                },
            }
            pickle.dump(produtos, arq_produtos)
            arq_produtos.close()
        return produtos
    def recuperar_clientes():
        try:
            arq_clientes = open("clientes.dat", "rb")
            clientes = pickle.load(arq_clientes)
            arq_clientes.close()
        except:
            arq_clientes = open("clientes.dat", "wb")
            clientes = {
                # [nome, telefone, cpf, data de nascimento, status de atividade]
                "11111111111": [
                    "Hadrianus da Silva Lima",
                    "83999999999",
                    "11111111111",
                    "12/09/2006",
                    True
                ],
                "22222222222": [
                    "Valeria pereira de medeiros",
                    "84988888888",
                    "22222222222",
                    "04/11/2005",
                    True
                ],
                "33333333333": [
                    "Marycele saraiva da silva",
                    "83977777777",
                    "33333333333",
                    "24/10/1982",
                    True
                ],
                "44444444444": [
                    "Roberto alves de lima",
                    "83966666666",
                    "44444444444",
                    "13/11/1982",
                    True
                ],
            }
            pickle.dump(clientes, arq_clientes)
            arq_clientes.close()
        return clientes
    
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
        print(" \  0- Voltar🔙                    /")
        print("  ---------------------------------")
        resp6 = input("Informe a opção desejada: ").strip()
        resp6_validas = ["0", "1", "2", "3", "4"]
        while not (resp6 in resp6_validas):
            resp6 = input("Informe uma opção válida: ").strip()
        if resp6 == "1":
            limpar_terminal()
            print(rosa_inicio+"--------------------------------"+rosa_final)
            print(rosa_inicio+"|       ADICIONAR VENDA        |"+rosa_final)
            print(rosa_inicio+"--------------------------------"+rosa_final)
            # titulo_menu_menor("ADICIONAR VENDA")
            print()
            id_venda = input("Informe o ID da venda: ").strip()
            while verificar_numeros(id_venda) == False:
                id_venda = input("APENAS NÚMEROS: ").strip()
            if id_venda not in vendas:
                cpf_cliente = input("Informe o CPF de quem comprou o(s) produto(s): ").strip()
                while validar_cpf(cpf_cliente) == False:
                    cpf_cliente = input("Informe um CPF válido: ").strip()
                if cpf_cliente in clientes:
                    nome = clientes[cpf_cliente][0]
                    dia_da_compra = input(
                            "Informe a data da compra no formato DD/MM/AAAA: "
                        ).strip()
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
                        quantidade = input(
                                "Informe quantas unidades do produto foram compradas: "
                            ).strip()
                        while verificar_numeros(quantidade) == False:
                            quantidade = input("APENAS NÚMEROS: ").strip()
                        quantidade = int(quantidade)
                        if categoria == "roupas":
                            index_preco = 4
                        else:
                            index_preco = 2
                        preco += produtos[categoria][codigo][index_preco] * quantidade
                        vendas[id_venda] = [
                            nome,
                            cpf_cliente,
                            dia_da_compra,
                            {codigo: quantidade},
                            preco,
                            True
                        ]
                        parar = (
                            input("Deseja adicionar outro produto? [S/N]: ")
                            .strip()
                            .upper()
                        )
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
                                quantidade = input(
                                        "Informe quantas unidades do produto foram compradas: "
                                    ).strip()
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
                                parar = (
                                    input("Deseja adicionar outro produto? [S/N]: ")
                                    .strip()
                                    .upper()
                                )
                            else:
                                print("Esse produto não existe na loja!")
                                parar = (
                                    input("Deseja adicionar outro produto? [S/N]: ")
                                    .strip()
                                    .upper()
                                )
                        print(f"PREÇO TOTAL: R${preco}")
                        print()
                        print("--------------------------------")
                        print("|       VENDA CADASTRADA✅    |")
                        print("--------------------------------")
                        print()
                        print(vendas)  # Verificação
                    else:
                        print("Esse produto não existe na loja!")
                else:
                    print("Esse cliente não está cadastrado no loja!")
                    print("Por favor realize o cadastro do cliente primeiro!")
            elif (id_venda in vendas) and (vendas[id_venda][5] == False):
                print("\033[1;32m----------------------------------\033[m")
                print(f"NOME: {vendas[id_venda][0]}")
                print(f"DATA DA VENDA: {vendas[id_venda][2]}")
                print(f"ID DA VENDA: {id_venda}")
                print("\033[1;32m----------------------------------\033[m")
                reativacao = input("Deseja reativar essa venda? [S/N]: ").strip().upper()
                if reativacao == "S":
                    vendas[id_venda][5] = True
                    print("--------------------------------")
                    print("|       VENDA CADASTRADA✅    |")
                    print("--------------------------------")
                else:
                    print("Reativação cancelada!")
            else:
                print("Esse ID já está cadastrado!")
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
                    dia_da_compra = input(
                        "Informe a data  CORRETA da compra no formato DD/MM/AAAA: "
                    ).strip()
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
                        quantidade = input(
                                "Informe quantas unidades do produto foram compradas: "
                            ).strip()
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
                        parar = (
                            input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                        )
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
                                quantidade = input(
                                        "Informe quantas unidades do produto foram compradas: "
                                    ).strip()
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
                                parar = (
                                    input("Deseja adicionar outro produto? [S/N]: ")
                                    .strip()
                                    .upper()
                                )
                            else:
                                print("Produto não encontrado!")
                                parar = (
                                    input("Deseja adicionar outro produto? [S/N]: ")
                                    .strip()
                                    .upper()
                                )
                        print()
                        print("--------------------------------")
                        print("|        VENDA EDITADA✅      |")
                        print("--------------------------------")
                        print()
                        print(vendas)  # Verificação
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
                    excluir = (
                        input("Digite S para confirmar a exclusão: ").strip().upper()
                    )
                    if excluir == "S":
                        vendas[id_venda][5] = False
                        #del vendas[id_venda]
                        print()
                        print("--------------------------------")
                        print("|        VENDA EXCLUÍDA✅      |")
                        print("--------------------------------")
                        print()
                        print(vendas)  # verificação
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Essa venda não está cadastrada!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        else:
            gravar_vendas(vendas)
            break