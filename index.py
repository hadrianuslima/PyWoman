import pickle
from validacoes import validar_cpf , validar_data , verificar_preco , verificar_letras , verificar_numeros , limpar_terminal, validar_fone


def recuperar_clientes():
    try:
        arq_clientes = open("clientes.dat", "rb")
        clientes = pickle.load(arq_clientes)
    except:
        arq_clientes = open("clientes.dat", "wb")
        clientes = {
            # [nome, telefone, cpf, data de nascimento]
            "12345678901": [
                "Hadrianus da Silva Lima",
                "9999999999",
                "12345678901",
                "12/09/2006",
            ],
            "23456789012": [
                "Valeria pereira de medeiros",
                "8888888888",
                "23456789012",
                "04/11/2005",
            ],
            "34567890123": [
                "Marycele saraiva da silva",
                "7777777777",
                "34567890123",
                "24/10/1982",
            ],
            "45678901234": [
                "Roberto alves de lima",
                "6666666666",
                "45678901234",
                "13/11/1982",
            ],
        }
        pickle.dump(clientes, arq_clientes)
    arq_clientes.close()
    return clientes

def recuperar_produtos():
    try:
        arq_produtos = open("produtos.dat", "rb")
        produtos = pickle.load(arq_produtos)
    except:
        arq_produtos = open("produtos.dat", "wb")
        produtos = {
            "roupas": {
                "123": ["blusa", "M", "123", "preto", 50.00],
                "234": ["vestido", "P", "234", "azul", 70.00],
                "345": ["calça", "G", "345", "vermelho", 40.00],
                "456": ["sutiã", "M", "456", "preto", 30.00],
            },
            "cosmeticos": {
                "567": ["maquiagem", "567", 70.00],
                "678": ["perfume", "678", 80.00],
                "789": ["hidratante", "789", 65.00],
                "890": ["óleo corporal", "890", 30.50],
            },
            "acessorios": {
                "901": ["pulseira", "901", 38.90],
                "012": ["colar", "012", 79.99],
                "112": ["óculos", "112", 58.99],
            },
        }
        pickle.dump(produtos, arq_produtos)
    arq_produtos.close()
    return produtos

def recuperar_vendas():
    try:
        arq_vendas = open("vendas.dat", "rb")
        vendas = pickle.load(arq_vendas)
    except:
        arq_vendas = open("vendas.dat", "wb")
        vendas = {  # Aqui nesse dicionário eu coloquei um ID para cada venda,
            # que recebe uma lista no qual tem o nome do cliente, CPF, data da venda,
            # um dicionário onde tem códigos do produto como chave e sua respectiva quantidade, e por ultimo o valor total da venda
            "11111": [
                "Hadrianus da silva lima",
                "12345678901",
                "11/11/2011",
                {"123": 3, "234": 2},
                1000.00,
            ],
            "22222": [
                "Valeria pereira de medeiros",
                "23456789012",
                "11/11/2011",
                {"123": 3, "234": 4},
                1500.00,
            ],
            "33333": [
                "Marycele saraiva da silva",
                "34567890123",
                "12/11/2011",
                {"234": 6, "345": 9},
                2000.00,
            ],
        }
        pickle.dump(vendas, arq_vendas)
    arq_vendas.close()
    return vendas

def gravar_clientes(clientes_loja):
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes_loja, arq_clientes)
    arq_clientes.close()

def gravar_produtos(produtos_loja):
    arq_produtos = open("produtos.dat", "wb")
    pickle.dump(produtos_loja, arq_produtos)
    arq_produtos.close()
    
def gravar_vendas(vendas_loja):
    arq_vendas = open("vendas.dat", "wb")
    pickle.dump(vendas_loja, arq_vendas)
    arq_vendas.close()

clientes = recuperar_clientes()
produtos = recuperar_produtos()
vendas = recuperar_vendas()

rosa_inicio = "\033[1;31;45m"
rosa_final = "\033[m"

modulo = ""
while modulo != "0":
    limpar_terminal()
    print(rosa_inicio+"--------------------------------"+rosa_final)
    print(rosa_inicio+"|           Py WOMAN           |"+rosa_final)
    print(rosa_inicio+"--------------------------------"+rosa_final) # As barras não estão totalmente alinhadas aqui, mas no terminal está
    print("|| 1- Clientes👤              ||")
    print("|| 2- Produtos🛍️               ||")
    print("|| 3- Vendas💵                ||")
    print("|| 4- Relatórios📄            ||")
    print("|| 5- Sobre o sistemaℹ️        ||")
    print(" \  0- Sair🔙                 //")
    print("  ---------------------------")
    modulo = input("Informe o módulo que deseja acessar: ").strip()
    modulos_validos = ["0", "1", "2", "3", "4", "5"]
    while not (modulo in modulos_validos):
        modulo = input("Informe uma opção válida: ").strip()
    while modulo == "1":
        limpar_terminal()
        print(rosa_inicio+"--------------------------------"+rosa_final)
        print(rosa_inicio+"|      MÓDULO DE CLIENTES      |"+rosa_final)
        print(rosa_inicio+"--------------------------------"+rosa_final)
        print("|| 1- Cadastrar cliente✅     ||")
        print("|| 2- Ver dados do clienteℹ️   ||")
        print("|| 3- Atualizar dados🔁       ||")
        print("|| 4- Excluir cadastro 🗑️      ||")
        print(" \  0- Voltar🔙                /")
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
            if not (cpf_cliente in clientes):
                nome = input("Informe o nome do cliente: ").strip().capitalize()
                while verificar_letras(nome) == False:
                    nome = input("Informe o nome CORRETO do cliente : ").strip().capitalize()
                fone = input("Informe o número do telefone do cliente: ").strip()
                while validar_fone(fone) == False:
                    fone = input("Informe o número válido: ").strip()
                data_nasc = input("Informe a data de nascimento do cliente no formato DD/MM/AAAA: ").strip()

                while validar_data(data_nasc) == False:
                   data_nasc = input("Informe a data válida no formato DD/MM/AAAA: ").strip()

                clientes[cpf_cliente] = [
                    nome,
                    fone,
                    cpf_cliente,
                    data_nasc,
                ]  # Add cliente no dicionário de clientes
                print()
                print("--------------------------------")
                print("|      CLIENTE CADASTRADO ✅   |")
                print("--------------------------------")
                print()
                print(clientes)
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
                if busca in clientes[i][0].lower():
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
            #titulo_menu_menor("ATUALIZAR DADOS")
            print()
            busca = input("NOME: ").strip().lower()
            while verificar_letras(busca) == False:
                    busca = input("SOMENTE LETRAS: ").strip().lower()
            achou = ""
            for i in clientes:
                if busca in clientes[i][0].lower():
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
                    data_nasc = input(
                            "Informe a nova data de nascimento para cliente: "
                        ).strip()
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
                    print(clientes)  # Verificação
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
                if busca in clientes[i][0].lower():
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
                    excluir = (
                        input("Digite S para excluir o cadastro: ").strip().upper()
                    )
                    if excluir == "S":
                        del clientes[cpf_cliente]
                        print("--------------------------------")
                        print("|       CADASTRO EXCLUÍDO✅    |")
                        print("--------------------------------")
                        print()
                        print(clientes)  # Verificação
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Esse CPF não está cadastrado!")
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
        else:
            break

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
                    ]  # Add peça de roupa dentro do dicionario de roupas que esta dentro do dicionario de produtos
                    print()
                    print("--------------------------------")
                    print("|       PEÇA CADASTRADA✅      |")
                    print("--------------------------------")
                    print()
                    print(produtos["roupas"])  # Verificação
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
                    if busca in produtos["roupas"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['roupas'][codigo][2]}")
                        print(f"PEÇA: {produtos['roupas'][codigo][0]}")
                        print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                        print(f"COR: {produtos['roupas'][codigo][3]}")
                        print(f"PREÇO: {produtos['roupas'][codigo][4]}")
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
                    if busca in produtos["roupas"][codigo][0].lower():
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
                            float(preco)
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
                    if busca in produtos["roupas"][codigo][0].lower():
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
                            del produtos["roupas"][codigo]
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
                    produtos["cosmeticos"][codigo] = [tipo_cosmetico, codigo, float(preco)]
                    print()
                    print("--------------------------------")
                    print("|     COSMÉTICO CADASTRADO✅   |")
                    print("--------------------------------")
                    print()
                    print(produtos["cosmeticos"])  # Vericação
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
                    if busca in produtos["cosmeticos"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
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
                    if busca in produtos["cosmeticos"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
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
                        print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
                        tipo_cosmetico = input("Informe o TIPO atualizado do cosmético: ").strip()
                        while verificar_letras(tipo_cosmetico) == False:
                            tipo_cosmetico = input("SOMENTE LETRAS : ").strip()
                        preco = input("Informe o novo VALOR para o cosmético: R$").strip()
                        while verificar_preco(preco) == False:
                            preco = input("Informe o valor do cosmético de forma correta: R$").strip()
                        produtos["cosmeticos"][codigo] = [tipo_cosmetico, codigo, float(preco)]
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
                    if busca in produtos["cosmeticos"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                        print(f"COSMÉTICO: {produtos['cosmeticos'][codigo][0]}")
                        print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
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
                        print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
                        excluir = (
                            input("Digite S para confirmar a exclusão: ")
                            .strip()
                            .upper()
                        )
                        print()
                        if excluir == "S":
                            del produtos["cosmeticos"][codigo]
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
                    produtos["acessorios"][codigo] = [tipo_acessorio, codigo, float(preco)]
                    print()
                    print("--------------------------------")
                    print("|     ACESSÓRIO CADASTRADO✅   |")
                    print("--------------------------------")
                    print()
                    print(produtos["acessorios"])  # Verificação
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
                    if busca in produtos["acessorios"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                        print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
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
                    if busca in produtos["acessorios"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                        print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
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
                        print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
                        print()
                        tipo_acessorio = input("Informe o tipo atualizado do acessório: ").strip()
                        while verificar_letras(tipo_acessorio) == False:
                            tipo_acessorio = input("SOMENTE LETRAS : ").strip()
                        preco = input("Informe o novo valor para o acessório: R$").strip()
                        while verificar_preco(preco) == False:
                            preco = input("Informe o valor do acessório de forma correta: R$").strip()
                        produtos["acessorios"][codigo] = [tipo_acessorio, codigo, float(preco)]
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
                    if busca in produtos["acessorios"][codigo][0].lower():
                        print("\033[1;32m----------------------------------\033[m")
                        print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                        print(f"ACESSÓRIO: {produtos['acessorios'][codigo][0]}")
                        print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
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
                        print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
                        print()
                        excluir = (
                            input("Digite S para confirmar a exclusão: ")
                            .strip()
                            .upper()
                        )
                        if excluir == "S":
                            del produtos["acessorios"][codigo]
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
                        vendas[id_venda].append(preco)
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
                if busca in vendas[id][0].lower():
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
                    print(f"PREÇO TOTAL: {vendas[id_venda][4]}")
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
                if busca in vendas[id][0].lower():
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
                    print(f"PREÇO TOTAL: {vendas[id_venda][4]}")
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
                        vendas[id_venda].append(preco)
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
                if busca in vendas[id][0].lower():
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
                    print(f"PREÇO TOTAL: {vendas[id_venda][4]}")
                    excluir = (
                        input("Digite S para confirmar a exclusão: ").strip().upper()
                    )
                    if excluir == "S":
                        del vendas[id_venda]
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
            break
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
        print(" \  0- Voltar                      /")
        print("  --------------------------------")
        resp7 = input("Informe a opção desejada: ").strip()
        resp7_validas = ["0", "1", "2", "3", "4", "5"]
        while not (resp7 in resp7_validas):
            resp7 = input("Informe uma opção válida: ").strip()
        if resp7 == "0":
            break
        else:
            print()
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print(rosa_inicio+"|    FUNÇÃO EM DESENVOLVIMENTO⚠️   |"+rosa_final)
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print()
            input("APERTE ENTER PARA PROSSEGUIR")

    if modulo == "5":
        limpar_terminal()
        print(rosa_inicio+"-------------------------------------------"+rosa_final)
        print(rosa_inicio+"|               SOBRE O SISTEMA           |"+rosa_final)
        print(rosa_inicio+"-------------------------------------------"+rosa_final)
        print("|| PROGRAMA PARA GESTÃO DE LOJA FEMININA ||")
        print("||           DESENVOLVIDO POR:           ||")
        print("|| 1- hadrianus.lima.130@ufrn.edu.br     ||")
        print("||              LICENÇA MIT              ||")
        print("||  https://opensource.org/licenses/MIT  ||")
        print(" \                                        /")
        print("  ---------------------------------------")
        input("APERTE ENTER PARA PROSSEGUIR")

print("PROGRAMA FECHADO")

gravar_clientes(clientes)
gravar_produtos(produtos)
gravar_vendas(vendas)