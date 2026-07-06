def relatorios():   
    from recup_dados import recuperar_clientes,recuperar_produtos,recuperar_vendas
    from validacoes import limpar_terminal, verificar_letras, validar_cpf

    rosa_inicio = "\033[1;31;45m"
    rosa_final = "\033[m"

    clientes = recuperar_clientes()
    vendas = recuperar_vendas()
    produtos = recuperar_produtos()

    modulo = "4"
    while modulo == "4":
        limpar_terminal()
        print(rosa_inicio+"------------------------------------"+rosa_final)
        print(rosa_inicio+"|        MÓDULO DE RELATÓRIOS      |"+rosa_final)
        print(rosa_inicio+"------------------------------------"+rosa_final)
        print("|| 1- Lista dos produtos          ||")
        print("|| 2- Lista de vendas             ||")
        print("|| 3- Lista de clientes           ||")
        print("|| 4- Produtos mais vendidos      ||")
        print("|| 5- Preferência de clientes     ||")
        print("||  0- Voltar                      /")
        print("  --------------------------------")
        resp7 = input("Informe a opção desejada: ").strip()
        resp7_validas = ["0", "1", "2", "3", "4", "5"]
        while not (resp7 in resp7_validas):
            resp7 = input("Informe uma opção válida: ").strip()
        if resp7 == "0":
            break
        elif resp7 == "1":
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|         LISTA DE PRODUTOS        |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            for categoria in produtos:
                if categoria == "roupas":
                    for codigo in produtos[categoria]:
                        if produtos[categoria][codigo][5] == True:
                            print("\033[1;32m----------------------------------\033[m")
                            print(f"CÓDIGO: {produtos[categoria][codigo][2]}")
                            print(f"PEÇA: {produtos[categoria][codigo][0]}")
                            print(f"TAMANHO: {produtos[categoria][codigo][1]}")
                            print(f"COR: {produtos[categoria][codigo][3]}")
                            print(f"PREÇO: R${produtos[categoria][codigo][4]}")
                            print("\033[1;32m----------------------------------\033[m")
                elif categoria == "cosmeticos":        
                    for codigo in produtos[categoria]:
                        if produtos[categoria][codigo][3] == True:
                            print("\033[1;32m----------------------------------\033[m")
                            print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                            print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                            print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                            print("\033[1;32m----------------------------------\033[m")
                else:
                    for codigo in produtos[categoria]:
                        if produtos[categoria][codigo][3] == True:
                            print("\033[1;32m----------------------------------\033[m")
                            print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                            print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                            print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                            print("\033[1;32m----------------------------------\033[m")
            input("APERTE ENTER PARA PROSSEGUIR")     
        elif resp7 == "2":
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|          LISTA DE VENDAS         |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            for id_venda in vendas:
                if vendas[id_venda][5] ==  True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"NOME: {vendas[id_venda][0]}")
                    print(f"CPF: {vendas[id_venda][1]}")
                    print(f"DATA: {vendas[id_venda][2]}")
                    print("PRODUTOS E QUANTIDADES:")
                    for i in vendas[id_venda][3]:
                        print("-", end=" ")
                        print(f"{i}: {vendas[id_venda][3][i]}")
                    print(f"PREÇO TOTAL: R${vendas[id_venda][4]}")
                    print("\033[1;32m----------------------------------\033[m")
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp7 == "3":
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|         LISTA DE CLIENTES        |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            for cpf_cliente in clientes:
                if clientes[cpf_cliente][4] == True:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CPF: {clientes[cpf_cliente][2]}")
                    print(f"NOME: {clientes[cpf_cliente][0]}")
                    print(f"TELEFONE: {clientes[cpf_cliente][1]}")
                    print(f"DATA DE NASCIMENTO: {clientes[cpf_cliente][3]}")
                    print("\033[1;32m----------------------------------\033[m")
            input("APERTE ENTER PARA PROSSEGUIR")
        elif resp7 == "4": 
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|      PRODUTOS MAIS VENDIDOS      |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            mais_vend = {}
            for id_venda in vendas:
                if vendas[id_venda][5] == True:
                    for cod_produt in vendas[id_venda][3]:
                        if cod_produt not in mais_vend:
                            mais_vend[cod_produt] = vendas[id_venda][3][cod_produt]
                        else:
                            mais_vend[cod_produt] += vendas[id_venda][3][cod_produt]
            mais_vend = dict(sorted(mais_vend.items(),key=lambda item: item[1], reverse=True))
            contador = 0 
            for produt in mais_vend:
                if contador == 5: #Mostrar somente os 5 produtos mais vendidos
                    break
                elif produt in produtos["roupas"]:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"Produto: {produtos["roupas"][produt][0]}")
                    print(f"Codigo: {produt}")
                    print(f"Quantidade: {mais_vend[produt]}")
                    print("\033[1;32m----------------------------------\033[m")
                elif produt in produtos["cosmeticos"]:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"Produto: {produtos["cosmeticos"][produt][0]}")
                    print(f"Codigo: {produt}")
                    print(f"Quantidade: {mais_vend[produt]}")
                    print("\033[1;32m----------------------------------\033[m")
                elif produt in produtos["acessorios"]:
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"Produto: {produtos["acessorios"][produt][0]}")
                    print(f"Codigo: {produt}")
                    print(f"Quantidade: {mais_vend[produt]}")
                    print("\033[1;32m----------------------------------\033[m")
                contador += 1
            input("APERTE ENTER PARA PROSSEGUIR")
        else:
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|      PREFERÊNCIA DE CLIENTES     |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            nome_client = input("Informe o nome do cliente que deseja ver as preferências: ").strip().lower()
            while verificar_letras(nome_client) == False:
                nome_client = input("SOMENTE LETRAS: ").strip().lower()
            achou = ""
            cpf_mostrados = []
            for id_venda in vendas:
                if nome_client in vendas[id_venda][0].lower() and vendas[id_venda][5] == True and vendas[id_venda][1] not in cpf_mostrados:
                    achou = "S"
                    cpf_mostrados += [vendas[id_venda][1]]
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CPF: {vendas[id_venda][1]}")
                    print(f"NOME: {vendas[id_venda][0]}")
                    print("\033[1;32m----------------------------------\033[m")
            if achou != "S":
                print("Esse cliente ainda não realizou compra.")
            else:
                cpf_cliente = input("Informe o CPF do cliente desejado: ").strip()
                while validar_cpf(cpf_cliente) == False:
                    cpf_cliente = input("Informe o CPF de forma correta: ").strip()
                prefe_client = {}
                for id_venda in vendas:
                    if cpf_cliente == vendas[id_venda][1] and vendas[id_venda][5] == True:
                        for cod_produt in vendas[id_venda][3]:
                            if cod_produt not in prefe_client:
                                prefe_client[cod_produt] = vendas[id_venda][3][cod_produt]
                            else:
                                prefe_client[cod_produt] += vendas[id_venda][3][cod_produt]
                prefe_client = dict(sorted(prefe_client.items(),key=lambda item: item[1], reverse=True))
                limpar_terminal()
                print(rosa_inicio+"------------------------------------"+rosa_final)
                print(rosa_inicio+"|      PREFERÊNCIA DE CLIENTES     |"+rosa_final)
                print(rosa_inicio+"------------------------------------"+rosa_final)
                print(f"CLIENTE: {clientes[cpf_cliente][0]}")
                contador = 0 
                for produt in prefe_client:
                    if contador == 5: #Mostrar somente os 5 produtos mais vendidos
                        break
                    elif produt in produtos["roupas"]:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"Produto: {produtos["roupas"][produt][0]}")
                        print(f"Codigo: {produt}")
                        print(f"Quantidade: {prefe_client[produt]}")
                        print("\033[1;32m----------------------------------\033[m")
                    elif produt in produtos["cosmeticos"]:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"Produto: {produtos["cosmeticos"][produt][0]}")
                        print(f"Codigo: {produt}")
                        print(f"Quantidade: {prefe_client[produt]}")
                        print("\033[1;32m----------------------------------\033[m")
                    elif produt in produtos["acessorios"]:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"Produto: {produtos["acessorios"][produt][0]}")
                        print(f"Codigo: {produt}")
                        print(f"Quantidade: {prefe_client[produt]}")
                        print("\033[1;32m----------------------------------\033[m")
                    contador += 1
            input("APERTE ENTER PARA PROSSEGUIR")