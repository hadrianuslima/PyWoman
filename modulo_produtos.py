def CRUD_produto():
    import pickle
    from validacoes import verificar_preco , verificar_letras , verificar_numeros , limpar_terminal

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
    
    def gravar_produtos(produtos_loja):
        arq_produtos = open("produtos.dat", "wb")
        pickle.dump(produtos_loja, arq_produtos)
        arq_produtos.close()

    rosa_inicio = "\033[1;31;45m"
    rosa_final = "\033[m"
    produtos = recuperar_produtos()
    modulo = "2"
    while modulo == "2":
        limpar_terminal()
        print(rosa_inicio+"--------------------------------"+rosa_final)
        print(rosa_inicio+"|      MÓDULO DE PRODUTOS      |"+rosa_final)
        print(rosa_inicio+"--------------------------------"+rosa_final)
        print("|| 1- Roupas👗                ||")
        print("|| 2- Cosméticos💄            ||")
        print("|| 3- Acessórios👓            ||")
        print(" \  0- Voltar 🔙               /")
        print("  ----------------------------")
        resp2 = input("Informe a opção que deseja: ").strip()
        resp2_validas = ["0", "1", "2", "3"]
        while not (resp2 in resp2_validas):
            resp2 = input("Informe uma opção válida: ").strip()
        if resp2 == "0":
            gravar_produtos(produtos)
            break
        while resp2 == "1":
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|         ROUPAS FEMININA          |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            #titulo_menu_maior("ROUPAS FEMININAS")
            print("|| 1- Cadastrar peça de roupa✅   ||")
            print("|| 2- Ver informações da peçaℹ️    ||")
            print("|| 3- Editar informações da peça🔁||")
            print("|| 4- Excluir peça🗑️               ||")
            print(" \  0- Voltar🔙                    /")
            print("   ------------------------------")
            resp3 = input("Informe a opção que deseja: ").strip()
            resp3_validas = ["0", "1", "2", "3", "4"]
            while not (resp3 in resp3_validas):
                resp3 = input("Informe uma opção válida: ").strip()
            if resp3 == "1":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|       CADASTRAR PEÇA         |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                codigo = input("Informe o código da peça: ").strip()
                while verificar_numeros(codigo) == False:
                    codigo = input("APENAS NÚMEROS: ").strip()
                if not (codigo in produtos["roupas"]):
                    tipo_peca = input("Informe o tipo de peça: ").strip()
                    while verificar_letras(tipo_peca) == False:
                        tipo_peca = input("SOMENTE LETRAS : ").strip()
                    tamanho = input("Informe o tamanho da peça: ").strip().upper()
                    cor = input("Informe a cor da peça: ").strip()
                    while verificar_letras(cor) == False:
                        cor = input("SOMENTE LETRAS : ").strip()
                    preco = input("Informe o valor da peça: R$").strip()
                    while verificar_preco(preco) == False:
                        preco = input("Informe o valor da peça de forma correta: R$").strip()
                    produtos["roupas"][codigo] = [
                        tipo_peca,
                        tamanho,
                        codigo,
                        cor,
                        float(preco),
                        True
                    ]  # Add peça de roupa dentro do dicionario de roupas que esta dentro do dicionario de produtos
                    print()
                    print("--------------------------------")
                    print("|       PEÇA CADASTRADA✅      |")
                    print("--------------------------------")
                    print()
                    print(produtos["roupas"])  # Verificação
                elif (codigo in produtos["roupas"]) and (produtos["roupas"][codigo][5] == False):
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CÓDIGO: {produtos['roupas'][codigo][2]}")
                    print(f"PEÇA: {produtos['roupas'][codigo][0]}")
                    print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                    print(f"COR: {produtos['roupas'][codigo][3]}")
                    print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                    print("\033[1;32m----------------------------------\033[m")
                    reativacao = input("Deseja recuperar os dados desse produto? [S/N]: ").strip().upper()
                    if reativacao == "S":
                        produtos["roupas"][codigo][5] = True
                        print("--------------------------------")
                        print("|       PEÇA CADASTRADA✅      |")
                        print("--------------------------------")
                    else:
                        print("Recadastro cancelado!")
                else:
                    print("Esse código de barras já está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp3 == "2":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|        DADOS DA PEÇA         |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("QUAL ROUPA DESEJA BUSCAR: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["roupas"]:
                    if busca in produtos["roupas"][codigo][0].lower() and produtos["roupas"][codigo][5] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['roupas'][codigo][2]}")
                        print(f"PEÇA: {produtos['roupas'][codigo][0]}")
                        print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                        print(f"COR: {produtos['roupas'][codigo][3]}")
                        print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Essa peça não está cadastrada!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp3 == "3":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|       ATUALIZAR PEÇA         |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("QUAL ROUPA DESEJA ATUALIZAR: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["roupas"]:
                    if busca in produtos["roupas"][codigo][0].lower() and produtos["roupas"][codigo][5] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['roupas'][codigo][2]}")
                        print(f"PEÇA: {produtos['roupas'][codigo][0]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Esse produto não está cadastrado!")
                else:
                    codigo = input("Informe o código da peça: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    if codigo in produtos["roupas"]:
                        print(f"TIPO: {produtos['roupas'][codigo][0]}")
                        print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                        print(f"COR: {produtos['roupas'][codigo][3]}")
                        print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                        cor = input("Informe a COR atualizada da peça: ").strip()
                        while verificar_letras(cor) == False:
                            cor = input("SOMENTE LETRAS : ").strip()
                        tipo_peca = input("Informe o TIPO atualizado da peça: ").strip()
                        while verificar_letras(tipo_peca) == False:
                            tipo_peca = input("SOMENTE LETRAS : ").strip()
                        tamanho = input("Informe o TAMANHO atualizado da peça: ").strip()
                        preco = input("Informe o novo VALOR da peça: R$").strip()
                        while verificar_preco(preco) == False:
                            preco = input("Informe o valor da peça de forma correta: R$").strip()
                        produtos["roupas"][codigo] = [
                            tipo_peca,
                            tamanho,
                            codigo,
                            cor,
                            float(preco),
                            True
                        ]
                        print()
                        print("--------------------------------")
                        print("|       PEÇA ATUALIZADA✅      |")
                        print("--------------------------------")
                        print(produtos["roupas"])  # Vericação
                    else:
                        print("Esse produto não está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp3 == "4":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|         EXCLUIR PEÇA         |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pela peça de deseja excluir: ").strip().lower()
                achou = ""
                for codigo in produtos["roupas"]:
                    if busca in produtos["roupas"][codigo][0].lower() and produtos["roupas"][codigo][5] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['roupas'][codigo][2]}")
                        print(f"PEÇA: {produtos['roupas'][codigo][0]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Nenhum produto encontrado!")
                else:
                    codigo = input("Informe o código da peça: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    if codigo in produtos["roupas"]:
                        print(f"TIPO: {produtos['roupas'][codigo][0]}")
                        print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                        print(f"COR: {produtos['roupas'][codigo][3]}")
                        print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                        print()
                        excluir = (
                            input("Digite S para confirmar a exclusão: ")
                            .strip()
                            .upper()
                        )
                        if excluir == "S":
                            produtos["roupas"][codigo][5] = False
                            #del produtos["roupas"][codigo]
                            print("--------------------------------")
                            print("|        PEÇA EXCLUÍDA✅        |")
                            print("--------------------------------")
                            print()
                            print(produtos["roupas"])  # Verificação
                        else:
                            print("Exclusão cancelada!")
                    else:
                        print("Esse produto não está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            else:
                break
        while resp2 == "2":
            limpar_terminal()
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print(rosa_inicio+"|        COSMÉTICOS FEMININOS      |"+rosa_final)
            print(rosa_inicio+"------------------------------------"+rosa_final)
            print("|| 1- Cadastrar cosméticos✅      ||")
            print("|| 2- Dados do cosméticoℹ️         ||")
            print("|| 3- Editar dados do cosmético🔁 ||")
            print("|| 4- Excluir cosmético🗑️          ||")
            print(" \  0- Voltar🔙                     / ")
            print("  --------------------------------")
            resp4 = input("Informe a opção que deseja: ").strip()
            resp4_validas = ["0", "1", "2", "3", "4"]
            while not (resp4 in resp4_validas):
                resp4 = input("Informe uma opção válida: ").strip()
            if resp4 == "1":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|     CADASTRAR COSMÉTICOS     |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                codigo = input("Informe o código do cosmético: ").strip()
                while verificar_numeros(codigo) == False:
                    codigo = input("APENAS NÚMEROS: ").strip()
                if not (codigo in produtos["cosmeticos"]):
                    tipo_cosmetico = input("Informe o tipo do cosmético: ").strip()
                    while verificar_letras(tipo_cosmetico) == False:
                        tipo_cosmetico = input("SOMENTE LETRAS : ").strip()
                    preco = input("Informe o valor do cosmético: R$").strip()
                    while verificar_preco(preco) == False:
                        preco = input("Informe o valor do cosmético de forma correta: R$").strip()
                    produtos["cosmeticos"][codigo] = [tipo_cosmetico, codigo, float(preco), True]
                    print()
                    print("--------------------------------")
                    print("|     COSMÉTICO CADASTRADO✅   |")
                    print("--------------------------------")
                    print()
                    print(produtos["cosmeticos"])  # Vericação
                elif (codigo in produtos["cosmeticos"]) and (produtos["cosmeticos"][codigo][3] == False):
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                    print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                    print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                    print("\033[1;32m----------------------------------\033[m")
                    reativacao = input("Deseja recadastrar esse produto? [S/N]: ").strip().upper()
                    if reativacao == "S":
                        produtos["cosmeticos"][codigo][3] = True
                        print("--------------------------------")
                        print("|     COSMÉTICO CADASTRADO✅   |")
                        print("--------------------------------")
                        print(produtos["cosmeticos"])
                    else:
                        print("Recadastro cancelado!")
                else:
                    print("Esse código já está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp4 == "2":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|      DADOS DO COSMÉTICO      |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pelo produto: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["cosmeticos"]:
                    if busca in produtos["cosmeticos"][codigo][0].lower() and produtos["cosmeticos"][codigo][3] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Produto não encontrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp4 == "3":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|         EDITAR DADOS         |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pelo produto que deseja editar: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["cosmeticos"]:
                    if busca in produtos["cosmeticos"][codigo][0].lower() and produtos["cosmeticos"][codigo][3] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Produto não encontrado!")
                else:
                    codigo = input("Informe o código do cosmético: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    print()
                    if codigo in produtos["cosmeticos"]:
                        print(f"TIPO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                        tipo_cosmetico = input("Informe o TIPO atualizado do cosmético: ").strip()
                        while verificar_letras(tipo_cosmetico) == False:
                            tipo_cosmetico = input("SOMENTE LETRAS : ").strip()
                        preco = input("Informe o novo VALOR para o cosmético: R$").strip()
                        while verificar_preco(preco) == False:
                            preco = input("Informe o valor do cosmético de forma correta: R$").strip()
                        produtos["cosmeticos"][codigo] = [tipo_cosmetico, codigo, float(preco), True]
                        print()
                        print("--------------------------------")
                        print("|       DADOS ATUALIZADOS✅    |")
                        print("--------------------------------")
                        print()
                        print(produtos["cosmeticos"])  # Verificação
                    else:
                        print("Não existe produto cadastrado com esse código!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp4 == "4":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|       EXCLUIR COSMÉTICO      |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pelo produto que deseja excluir: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["cosmeticos"]:
                    if busca in produtos["cosmeticos"][codigo][0].lower() and produtos["cosmeticos"][codigo][3] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Produto não encontrado!")
                else:
                    codigo = input("CÓDIGO: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    if codigo in produtos["cosmeticos"]:
                        print(f"TIPO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"PREÇO: R${produtos['cosmeticos'][codigo][2]}")
                        excluir = (
                            input("Digite S para confirmar a exclusão: ")
                            .strip()
                            .upper()
                        )
                        print()
                        if excluir == "S":
                            produtos["cosmeticos"][codigo][3] = False
                            #del produtos["cosmeticos"][codigo]
                            print("--------------------------------")
                            print("|      COSMÉTICO EXCLUÍDO✅    |")
                            print("--------------------------------")
                            print()
                            print(produtos["cosmeticos"])  # Verificação
                        else:
                            print("Exclusão cancelada!")
                    else:
                        print("Produto não encontrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            else:
                break
        while resp2 == "3":
            limpar_terminal()
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print(rosa_inicio+"|        ACESSÓRIOS FEMININOS     |"+rosa_final)
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print("|| 1- Cadastrar acessório✅      ||")
            print("|| 2- Dados do acessórioℹ️        ||")
            print("|| 3- Editar dados do acessório🔁||")
            print("|| 4- Excluir acessório🗑️         ||")
            print(" \  0- Voltar🔙                   /")
            print("  ------------------------------")
            resp5 = input("Informe a opção que deseja: ").strip()
            resp5_validas = ["0", "1", "2", "3", "4"]
            while not (resp5 in resp5_validas):
                resp5 = input("Informe uma opção válida: ").strip()
            if resp5 == "1":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|     CADASTRAR ACESSÓRIO      |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                codigo = input("Informe o código do acessório: ").strip()
                while verificar_numeros(codigo) == False:
                    codigo = input("APENAS NÚMEROS: ").strip()
                if not (codigo in produtos["acessorios"]):
                    tipo_acessorio = input("Informe o tipo do acessório: ").strip()
                    while verificar_letras(tipo_acessorio) == False:
                        tipo_acessorio = input("SOMENTE LETRAS : ").strip()
                    preco = input("Informe o valor do acessório: R$").strip()
                    while verificar_preco(preco) == False:
                        preco = input("Informe o valor do acessório de forma correta: R$").strip()
                    produtos["acessorios"][codigo] = [tipo_acessorio, codigo, float(preco), True]
                    print()
                    print("--------------------------------")
                    print("|     ACESSÓRIO CADASTRADO✅   |")
                    print("--------------------------------")
                    print()
                    print(produtos["acessorios"])  # Verificação
                elif (codigo in produtos["acessorios"]) and (produtos["acessorios"][codigo][3] == False):
                    print("\033[1;32m----------------------------------\033[m")
                    print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                    print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                    print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                    print("\033[1;32m----------------------------------\033[m")
                    reativacao = input("Deseja recadastrar esse produto? [S/N]: ").strip().upper()
                    if reativacao == "S":
                        produtos["acessorios"][codigo][3] = True
                        print("--------------------------------")
                        print("|     ACESSÓRIO CADASTRADO✅   |")
                        print("--------------------------------")
                    else:
                        print("Recadastro cancelado!")
                else:
                        print("Esse código já está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp5 == "2":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|      DADOS DO ACESSÓRIO      |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pelo acessório: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["acessorios"]:
                    if busca in produtos["acessorios"][codigo][0].lower() and produtos["acessorios"][codigo][3] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                        print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Produto não encontrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp5 == "3":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|        EDITAR DADOS          |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pelo acessório: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["acessorios"]:
                    if busca in produtos["acessorios"][codigo][0].lower() and produtos["acessorios"][codigo][3] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                        print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Produto não encontrado!")
                else:
                    codigo = input("Informe o código do acessório: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    if codigo in produtos["acessorios"]:
                        print()
                        print(f"TIPO: {produtos['acessorios'][codigo][0]}")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                        print()
                        tipo_acessorio = input("Informe o tipo atualizado do acessório: ").strip()
                        while verificar_letras(tipo_acessorio) == False:
                            tipo_acessorio = input("SOMENTE LETRAS : ").strip()
                        preco = input("Informe o novo valor para o acessório: R$").strip()
                        while verificar_preco(preco) == False:
                            preco = input("Informe o valor do acessório de forma correta: R$").strip()
                        produtos["acessorios"][codigo] = [tipo_acessorio, codigo, float(preco), True]
                        print()
                        print("--------------------------------")
                        print("|       DADOS ATUALIZADOS✅    |")
                        print("--------------------------------")
                        print()
                        print(produtos["acessorios"])  # Verificação
                    else:
                        print("Esse código não está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            elif resp5 == "4":
                limpar_terminal()
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print(rosa_inicio+"|      EXCLUIR ACESSÓRIO       |"+rosa_final)
                print(rosa_inicio+"--------------------------------"+rosa_final)
                print()
                busca = input("Busque pelo acessório: ").strip().lower()
                while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS : ").strip().lower()
                achou = ""
                for codigo in produtos["acessorios"]:
                    if busca in produtos["acessorios"][codigo][0].lower() and produtos["acessorios"][codigo][3] == True:
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                        print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                        print("\033[1;32m----------------------------------\033[m")
                        achou = "S"
                if achou != "S":
                    print("Produto não encontrado!")
                else:
                    codigo = input("CÓDIGO: ").strip()
                    while verificar_numeros(codigo) == False:
                        codigo = input("APENAS NÚMEROS: ").strip()
                    if codigo in produtos["acessorios"]:
                        print()
                        print(f"TIPO: {produtos['acessorios'][codigo][0]}")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"PREÇO: R${produtos['acessorios'][codigo][2]}")
                        print()
                        excluir = (
                            input("Digite S para confirmar a exclusão: ")
                            .strip()
                            .upper()
                        )
                        if excluir == "S":
                            produtos["acessorios"][codigo][3] = False
                            #del produtos["acessorios"][codigo]
                            print()
                            print("--------------------------------")
                            print("|      ACESSÓRIO EXCLUÍDO✅    |")
                            print("--------------------------------")
                            print()
                            print(produtos["acessorios"])  # Verificação
                        else:
                            print("Exclusão cancelada!")
                    else:
                        print("Esse código não está cadastrado!")
                print()
                input("APERTE ENTER PARA PROSSEGUIR")
            else:
                break