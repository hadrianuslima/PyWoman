import os

clientes = {
          #[nome, idade, telefone, cpf]
    "123": ['Hadrianus', '19', "9999999999", '123'],
    "234": ['Valeria', '20', '8888888888', '234'],
    "345": ['Marycele', '44', '7777777777', '345'],
    "456": ['Roberto', '44', '6666666666', '456']

}

produtos = {
    "roupas" :  {
                    "123": ['blusa', 'M', '123', 'preto', '50.00'],
                    "234": ['vestido', 'P', '234', 'azul', '70.00'],
                    "345": ['calça', 'G', '345', 'vermelho',  '40.00'],
                    "456": ['sutiã', 'M', '456', 'preto', '30.00']
    },
    "cosmeticos" : {

                    "567": ['maquiagem', '567', '70.00'],
                    "678": ['perfume', '678', '80.00'],
                    "789": ['hidratante', '789', '65.00'],
                    "890": ['óleo corporal', '890', '30.50']

    },
    "acessorios" : {

                    "901": ['pulseira', '901', '38.90'],
                    "012": ['colar', '012', '79.99'],
                    "112": ['óculos', '112', '58.99']

    }
}

vendas = { # Aqui nesse dicionário eu coloquei um ID para cada venda, 
            #que recebe uma lista no qual tem o CPF, data da venda, 
            #um dicionário onde tem códigos do produto como chave e sua respectiva quantidade, e por ultimo o valor total da venda
    
    "11111": ['123',
            '11/11/2011',  
            {
                "123": '3',
                "234": '2'
            },
            '1000.00'],

    "22222": ['234',
            '11/11/2011',  
            {
                "123": '3',
                "234": '4'
            },
            '1500.00'],
    "33333": ['345',
              '12/11/2011',
              {
                  "234": '6',
                  "345": '9'
              },
              '2000.00']

}

modulo = ""

while modulo != "0":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;31;45m--------------------------------\033[m")
    print("\033[1;31;45m|           Py WOMAN           |\033[m")
    print("\033[1;31;45m--------------------------------\033[m")
    # As barras não estão totalmente alinhadas aqui, mas no terminal está
    print("|| 1- Clientes👤              ||")
    print("|| 2- Produtos🛍️               ||")
    print("|| 3- Vendas💵                ||")
    print("|| 4- Relatórios📄            ||")
    print("|| 5- Sobre o sistemaℹ️        ||")
    print("\\\ 0- Sair🔙                 //")
    print("  ---------------------------")
    modulo = input("Informe o módulo que deseja acessar: ").strip()
    modulos_validos = ["0", "1", "2", "3", "4", "5"]
    while not(modulo in modulos_validos):
        modulo = input("Informe uma opção válida: ").strip()
    while modulo == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;31;45m--------------------------------\033[m")
        print("\033[1;31;45m|      MÓDULO DE CLIENTES      |\033[m")
        print("\033[1;31;45m--------------------------------\033[m")
        print("|| 1- Cadastrar cliente✅     ||")
        print("|| 2- Ver dados do clienteℹ️   ||")
        print("|| 3- Atualizar dados🔁       ||")
        print("|| 4- Excluir cadastro 🗑️      ||")
        print("\\\ 0- Voltar🔙                //")
        print("  ----------------------------")
        resp1 = input("Informe a opção que deseja: ").strip()
        resp1_validas = ["0", "1", "2", "3", "4"]
        while not(resp1 in resp1_validas):
            resp1 = input("Informe uma opção válida: ").strip()
        if resp1 == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|      CADASTRAR CLIENTE       |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            print()
            cpf = input("Informe o CPF do cliente: ").strip()
            if not(cpf in clientes):
                nome = input("Informe o nome do cliente: ").strip()
                idade = input("Informe a idade do cliente: ").strip()
                fone = input("Informe o número do telefone do cliente: ").strip()
                clientes[cpf] = [nome,idade,fone,cpf] #Add cliente no dicionário de clientes
                print()
                print("--------------------------------")
                print("|      CLIENTE CADASTRADO ✅   |")
                print("--------------------------------")
                print()
                print(clientes) #Verificação
            else:
                print("Esse CPF já está cadastrado!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')
        elif resp1 == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|       DADOS DO CLIENTEℹ️      |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            print()
            cpf = input("CPF: ").strip()
            if cpf in clientes:
                print(f"NOME: {clientes[cpf][0]}")
                print(f"CPF: {clientes[cpf][3]}")
                print(f"TELEFONE: {clientes[cpf][2]}")
                print(f"IDADE: {clientes[cpf][1]} anos")
            else:
                print("Cliente não encontrado!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')
        elif resp1 == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|       ATUALIZAR DADOS        |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            print()
            cpf = input("CPF: ").strip()
            if cpf in clientes:
                print(f"NOME: {clientes[cpf][0]}")
                print(f"TELEFONE: {clientes[cpf][2]}")
                print(f"IDADE: {clientes[cpf][1]} anos")
                nome = input("Informe o novo nome para o cliente: ").strip()
                idade = input("Informe a nova idade para cliente: ").strip()
                fone = input("Informe o novo número telefone cliente: ").strip()
                clientes[cpf][0] = nome
                clientes[cpf][1] = idade
                clientes[cpf][2] = fone
                print()
                print("--------------------------------")
                print("|      DADOS ATUALIZADOS✅     |")
                print("--------------------------------")
                print(clientes)  #Verificação
            else:
                print("Cliente não encontrado!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')
        elif resp1 == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|        EXCLUIR CADASTRO 🗑️    |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            print()
            cpf = input("CPF: ").strip()
            if cpf in clientes:
                print(f"NOME: {clientes[cpf][0]}")
                print(f"CPF: {clientes[cpf][3]}")
                print(f"TELEFONE: {clientes[cpf][2]}")
                print(f"IDADE: {clientes[cpf][1]} anos")
                excluir = input("Digite S para excluir o cadastro: ").strip().upper()
                if excluir == "S":
                    del clientes[cpf]
                    print("--------------------------------")
                    print("|      CADASTRO EXCLUÍDO✅    |")
                    print("--------------------------------")
                    print()
                    print(clientes) #Verificação
                else:
                    print("Exclusão cancelada!")
                    print()
            else:
                print("Cliente não encontrado!")
                print()
            input('APERTE ENTER PARA PROSSEGUIR')
        else:
            break

    while modulo == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;31;45m--------------------------------\033[m")
        print("\033[1;31;45m|      MÓDULO DE PRODUTOS      |\033[m")
        print("\033[1;31;45m--------------------------------\033[m")
        print("|| 1- Roupas👗                ||")
        print("|| 2- Cosméticos💄            ||")
        print("|| 3- Acessórios👓            ||")
        print("\\\ 0- Voltar 🔙             //")
        print("  ----------------------------")
        resp2 = input("Informe a opção que deseja: ").strip()
        resp2_validas = ["0", "1", "2", "3"]
        while not(resp2 in resp2_validas):
            resp2 = input("Informe uma opção válida: ").strip()
        if resp2 == "0":
            break
        while resp2 == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m------------------------------------\033[m")
            print("\033[1;31;45m|         ROUPAS FEMININA          |\033[m")
            print("\033[1;31;45m------------------------------------\033[m")
            print("|| 1- Cadastrar peça de roupa✅   ||")
            print("|| 2- Ver informações da peçaℹ️    ||")
            print("|| 3- Editar informações da peça🔁||")
            print("|| 4- Excluir peça🗑️               ||")
            print("\\\ 0- Voltar🔙                    //")
            print("   ------------------------------")
            resp3 = input("Informe a opção que deseja: ").strip()
            resp3_validas = ["0", "1", "2", "3", "4"]
            while not(resp3 in resp3_validas):
                resp3 = input("Informe uma opção válida: ").strip()
            if resp3 == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|       CADASTRAR PEÇA         |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código da peça: ").strip()
                if not(codigo in produtos["roupas"]):
                    tipo_peça = input("Informe o tipo de peça: ").strip()
                    tamanho = input("Informe o tamanho da peça: ").strip().upper()
                    cor = input("Informe a cor da peça: ").strip()
                    preco = input("Informe o valor da peça: R$").strip()
                    produtos["roupas"][codigo] = [tipo_peça, tamanho, codigo, cor, preco] #Add peça de roupa dentro do dicionario de roupas que esta dentro do dicionario de produtos
                    print()
                    print("--------------------------------")
                    print("|       PEÇA CADASTRADA✅      |")
                    print("--------------------------------")
                    print()
                    print(produtos["roupas"]) #Verificação
                else:
                    print("Esse código de barras já está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp3 == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|        DADOS DA PEÇA         |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código da peça: ").strip()
                print()
                if codigo in produtos["roupas"]:
                    print(f"TIPO: {produtos['roupas'][codigo][0]}")
                    print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                    print(f"CÓDIGO: {produtos['roupas'][codigo][2]}")
                    print(f"COR: {produtos['roupas'][codigo][3]}")
                    print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                else:
                    print("Essa peça não está cadastrada!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp3 == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|       ATUALIZAR PEÇA         |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código da peça: ").strip()
                if codigo in produtos["roupas"]:
                    print(f"TIPO: {produtos['roupas'][codigo][0]}")
                    print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                    print(f"COR: {produtos['roupas'][codigo][3]}")
                    print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                    cor = input("Informe a COR atualizada da peça: ").strip()
                    tipo_peça = input("Informe o TIPO atualizado da peça: ").strip()
                    tamanho = input("Informe o TAMANHO atualizado da peça: ").strip()
                    preco = input("Informe o novo VALOR da peça: R$").strip()
                    produtos["roupas"][codigo] = [tipo_peça, tamanho, codigo, cor, preco]
                    print()
                    print("--------------------------------")
                    print("|       PEÇA ATUALIZADA✅      |")
                    print("--------------------------------")
                    print(produtos["roupas"]) #Vericação
                else:
                    print("Esse produto não está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp3 == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|         EXCLUIR PEÇA         |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("CÓDIGO DA PEÇA: ").strip()
                if codigo in produtos["roupas"]:
                    print(f"TIPO: {produtos['roupas'][codigo][0]}")
                    print(f"TAMANHO: {produtos['roupas'][codigo][1]}")
                    print(f"COR: {produtos['roupas'][codigo][3]}")
                    print(f"PREÇO: R${produtos['roupas'][codigo][4]}")
                    print()
                    excluir = input("Digite S para confirmar a exclusão: ").strip().upper()
                    if excluir == "S":
                        del produtos["roupas"][codigo]
                        print("--------------------------------")
                        print("|        PEÇA EXCLUÍDA✅        |")
                        print("--------------------------------")
                        print()
                        print(produtos["roupas"]) #Verificação
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Esse produto não está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            else:
                break
        while resp2 == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m-----------------------------------\033[m")
            print("\033[1;31;45m|       COSMÉTICOS FEMININOS      |\033[m")
            print("\033[1;31;45m-----------------------------------\033[m")
            print("|| 1- Cadastrar cosméticos✅     ||")
            print("|| 2- Dados do cosméticoℹ️        ||")
            print("|| 3- Editar dados do cosmético🔁||")
            print("|| 4- Excluir cosmético🗑️         ||")
            print("\\\ 0- Voltar🔙                   // ")
            print("  -------------------------------")
            resp4 = input('Informe a opção que deseja: ').strip()
            resp4_validas = ["0", "1", "2", "3", "4"]
            while not(resp4 in resp4_validas):
                resp4 = input("Informe uma opção válida: ").strip()
            if resp4 == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|     CADASTRAR COSMÉTICOS     |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código do cosmético: ").strip()
                if not(codigo in produtos["cosmeticos"]):
                    tipo_cosmetico = input("Informe o tipo do cosmético: ").strip()
                    preco = input("Informe o valor do cosmético: R$").strip()
                    produtos["cosmeticos"][codigo] = [tipo_cosmetico, codigo, preco]
                    print()
                    print("--------------------------------")
                    print("|     COSMÉTICO CADASTRADO✅   |")
                    print("--------------------------------")
                    print()
                    print(produtos["cosmeticos"]) #Vericação
                else:
                    print("Esse código já está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp4 == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|      DADOS DO COSMÉTICO      |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código do cosmético: ").strip()
                print()
                if codigo in produtos["cosmeticos"]:
                    print(f"TIPO: {produtos['cosmeticos'][codigo][0]}")
                    print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                    print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
                else:
                    print("Esse cosmético não está cadastrado!")
                print()    
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp4 == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|         EDITAR DADOS         |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código do cosmético: ").strip()
                print()
                if codigo in produtos["cosmeticos"]:
                    print(f"TIPO: {produtos['cosmeticos'][codigo][0]}")
                    print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                    print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
                    tipo_cosmetico = input("Informe o TIPO atualizado do cosmético: ").strip()
                    preco = input("Informe o novo VALOR para o cosmético: R$").strip()
                    produtos["cosmeticos"][codigo] = [tipo_cosmetico, codigo, preco]
                    print()
                    print("--------------------------------")
                    print("|       DADOS ATUALIZADOS✅    |")
                    print("--------------------------------")
                    print()
                    print(produtos["cosmeticos"]) #Verificação
                else:
                    print("Não existe produto cadastrado com esse código!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp4 == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|       EXCLUÍR COSMÉTICO      |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("CÓDIGO: ").strip()
                if codigo in produtos["cosmeticos"]:
                    print(f"TIPO: {produtos['cosmeticos'][codigo][0]}")
                    print(f"CÓDIGO: {produtos['cosmeticos'][codigo][1]}")
                    print(f"PREÇO: {produtos['cosmeticos'][codigo][2]}")
                    excluir = input("Digite S para confirmar a exclusão: ").strip().upper()
                    print()
                    if excluir == "S":
                        del produtos["cosmeticos"][codigo]
                        print("--------------------------------")
                        print("|      COSMÉTICO EXCLUÍDO✅    |")
                        print("--------------------------------")
                        print()
                        print(produtos["cosmeticos"]) #Verificação
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Não existe cosmético cadastrado com esse código!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            else:
                break
        while resp2 == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[1;31;45m-----------------------------------\033[m")
            print("\033[1;31;45m|       ACESSÓRIOS FEMININOS      |\033[m")
            print("\033[1;31;45m-----------------------------------\033[m")
            print("|| 1- Cadastrar acessório✅      ||")
            print("|| 2- Dados do acessórioℹ️        ||")
            print("|| 3- Editar dados do acessório🔁||")
            print("|| 4- Excluir acessório🗑️         ||")
            print("\\\ 0- Voltar🔙                   //")
            print("  ------------------------------")
            resp5 = input('Informe a opção que deseja: ').strip()
            resp5_validas = ["0", "1", "2", "3", "4"]
            while not(resp5 in resp5_validas):
                resp5 = input("Informe uma opção válida: ").strip()
            if resp5 == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|     CADASTRAR ACESSÓRIO      |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código do acessório: ").strip()
                if not(codigo in produtos["acessorios"]):
                    tipo_acessorio = input("Informe o tipo do acessório: ").strip()
                    preco = input("Informe o valor do acessório: R$").strip()
                    produtos["acessorios"][codigo] = [tipo_acessorio, codigo, preco]
                    print()
                    print("--------------------------------")
                    print("|     ACESSÓRIO CADASTRADO✅   |")
                    print("--------------------------------")
                    print()
                    print(produtos["acessorios"]) # Verificação
                else:
                    print("Esse código já está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp5 == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|      DADOS DO ACESSÓRIO      |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código do acessório: ").strip()
                if codigo in produtos["acessorios"]:
                    print()
                    print(f"TIPO: {produtos['acessorios'][codigo][0]}")
                    print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                    print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
                else:
                    print("Esse código não está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp5 == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|        EDITAR DADOS          |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("Informe o código do acessório: ").strip()
                if codigo in produtos["acessorios"]:
                    print()
                    print(f"TIPO: {produtos['acessorios'][codigo][0]}")
                    print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                    print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
                    print()
                    tipo_acessorio = input("Informe o tipo atualizado do acessório: ").strip()
                    preco = input("Informe o novo valor para o acessório: R$").strip()
                    produtos["acessorios"][codigo] = [tipo_acessorio, codigo, preco]
                    print()
                    print("--------------------------------")
                    print("|       DADOS ATUALIZADOS✅    |")
                    print("--------------------------------")
                    print()
                    print(produtos["acessorios"]) #Verificação
                else:
                    print("Esse código não está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            elif resp5 == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[1;31;45m--------------------------------\033[m")
                print("\033[1;31;45m|      EXCLUIR ACESSÓRIO       |\033[m")
                print("\033[1;31;45m--------------------------------\033[m")
                print()
                codigo = input("CÓDIGO: ").strip()
                if codigo in produtos["acessorios"]:
                    print()
                    print(f"TIPO: {produtos['acessorios'][codigo][0]}")
                    print(f"CÓDIGO: {produtos['acessorios'][codigo][1]}")
                    print(f"PREÇO: {produtos['acessorios'][codigo][2]}")
                    print()
                    excluir = input("Digite S para confirmar a exclusão: ").strip().upper()
                    if excluir == "S":
                        del produtos["acessorios"][codigo]
                        print()
                        print("--------------------------------")
                        print("|      ACESSÓRIO EXCLUÍDO✅    |")
                        print("--------------------------------")
                        print()
                        print(produtos["acessorios"]) #Verificação
                    else:
                        print("Exclusão cancelada!")
                else:
                    print("Esse código não está cadastrado!")
                print()
                input('APERTE ENTER PARA PROSSEGUIR')
            else:
                break
    while modulo == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;31;45m-----------------------------------\033[m")
        print("\033[1;31;45m|          MÓDULO DE VENDAS       |\033[m")
        print("\033[1;31;45m-----------------------------------\033[m")
        print("|| 1- Adicionar venda✅          ||")
        print("|| 2- Visualizar vendasℹ️         ||")
        print("|| 3- Editar venda🔁             ||")
        print("|| 4- Excluir uma venda🗑️         ||")
        print("\\\ 0- Voltar🔙                   //")
        print("  --------------------------------")
        resp6 = input("Informe a opção desejada: ").strip()
        resp6_validas = ["0", "1", "2", "3", "4"]
        while not(resp6 in resp6_validas):
                resp6 = input("Informe uma opção válida: ").strip()
        if resp6 == "1":
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|       ADICIONAR VENDA        |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            print()
            id_venda = input("Informe o ID da venda: ").strip()
            if id_venda not in vendas:
                cpf = input("Informe o CPF de quem comprou o(s) produto(s): ").strip()
                dia_da_compra = input("Informe a data da compra no formato DD/MM/AAAA: ").strip()
                codigo = input("Informe o código do produto: ").strip()
                quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                vendas[id_venda] = [cpf, dia_da_compra, {codigo : quantidade}]
                parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                while parar != "N":
                    codigo = input("Informe o código do produto: ").strip()
                    quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                    vendas[id_venda][2][codigo] = quantidade   
                    parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                preco= input("Informe o preço TOTAL da compra: R$").strip()
                vendas[id_venda].append(preco)
                print()
                print("--------------------------------")
                print("|       VENDA CADASTRADA✅    |")
                print("--------------------------------")
                print()
                print(vendas) #Verificação
            else:
                print("Esse ID já está cadastrado!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')
        elif resp6 == "2":
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|      VISUALIZAR VENDAS       |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            id_venda = input("Informe o ID da venda que deseja visualizar: ").strip()
            if id_venda in vendas:
                print()
                print(f"CPF: {vendas[id_venda][0]}")
                print(f"DATA: {vendas[id_venda][1]}")
                print("PRODUTOS E QUANTIDADES:")
                for i in vendas[id_venda][2]:
                    print("-", end= " ")
                    print(f"{i}: {vendas[id_venda][2][i]}")
                print(f"PREÇO TOTAL: {vendas[id_venda][3]}")
            else:
                print("Essa venda não está cadastrada!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')
        elif resp6 == "3":
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|        EDITAR VENDA          |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            id_venda = input("Informe o ID da venda que deseja editar: ").strip()
            if id_venda in vendas:
                print()
                print(f"CPF: {vendas[id_venda][0]}")
                print(f"DATA: {vendas[id_venda][1]}")
                print("PRODUTOS E QUANTIDADES:")
                for i in vendas[id_venda][2]:
                    print("-", end= " ")
                    print(f"{i}: {vendas[id_venda][2][i]}")
                print(f"PREÇO TOTAL: {vendas[id_venda][3]}")
                print()
                cpf = input("Informe o CPF CORRETO de quem comprou o(s) produto(s): ").strip()
                dia_da_compra = input("Informe a data  CORRETA da compra no formato DD/MM/AAAA: ").strip()
                codigo = input("Informe o código CORRETO do produto: ").strip()
                quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                vendas[id_venda] = [cpf, dia_da_compra, {codigo : quantidade}]
                parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                while parar != "N":
                    codigo = input("Informe o código do produto: ").strip()
                    quantidade = input("Informe quantas unidades do produto foram compradas: ").strip()
                    vendas[id_venda][2][codigo] = quantidade   
                    parar = input("Deseja adicionar outro produto? [S/N]: ").strip().upper()
                preco= input("Informe o preço TOTAL CORRETO da compra: R$").strip()
                vendas[id_venda].append(preco)
                print()
                print("--------------------------------")
                print("|        VENDA EDITADA✅      |")
                print("--------------------------------")
                print()
                print(vendas) #Verificação
            else:
                print("Esse ID não está cadastrado!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')
        elif resp6 == "4":
            print("\033[1;31;45m--------------------------------\033[m")
            print("\033[1;31;45m|        EXCLUIR VENDA         |\033[m")
            print("\033[1;31;45m--------------------------------\033[m")
            print()
            id_venda = input("Informe o ID da venda que deseja excluir: ").strip()
            if id_venda in vendas:
                print()
                print(f"CPF: {vendas[id_venda][0]}")
                print(f"DATA: {vendas[id_venda][1]}")
                print("PRODUTOS E QUANTIDADES:")
                for i in vendas[id_venda][2]:
                    print("-", end= " ")
                    print(f"{i}: {vendas[id_venda][2][i]}")
                print(f"PREÇO TOTAL: {vendas[id_venda][3]}")
                excluir = input("Digite S para confirmar a exclusão: ").strip().upper()
                if excluir == "S":
                    del vendas[id_venda]
                    print()
                    print("--------------------------------")
                    print("|        VENDA EXCLUÍDA✅      |")
                    print("--------------------------------") 
                    print()
                    print(vendas) #verificação
                else:
                    print("Exclusão cancelada!") 
            else:
                print("Essa venda não está cadastrada!")
            print()
            input('APERTE ENTER PARA PROSSEGUIR') 
        else:
            break       
    while modulo == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;31;45m-----------------------------------\033[m")
        print("\033[1;31;45m|        MÓDULO DE RELATÓRIOS     |\033[m")
        print("\033[1;31;45m-----------------------------------\033[m")
        print("|| 1- Lista dos produtos         ||")
        print("|| 2- Lista de vendas            ||")
        print("|| 3- Lista de clientes          ||")
        print("|| 4- Produtos mais vendidos     ||")
        print("|| 5- Preferência de clientes    ||")
        print("\\\ 0- Voltar                    //")
        print("  -------------------------------")
        resp7 = input("Informe a opção desejada: ").strip()
        resp7_validas = ["0", "1", "2", "3", "4", "5"]
        while not(resp7 in resp7_validas):
            resp7 = input("Informe uma opção válida: ").strip()
        if resp7 == "0":
            break
        else:
            print()
            print("\033[1;31;45m-----------------------------------\033[m")
            print("\033[1;31;45m|    FUNÇÃO EM DESENVOLVIMENTO⚠️   |\033[m")
            print("\033[1;31;45m-----------------------------------\033[m")
            print()
            input('APERTE ENTER PARA PROSSEGUIR')

    if modulo == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;31;45m-------------------------------------------\033[m")
        print("\033[1;31;45m|               SOBRE O SISTEMA           |\033[m")
        print("\033[1;31;45m-------------------------------------------\033[m")
        print("|| PROGRAMA PARA GESTÃO DE LOJA FEMININA ||")
        print("||           DESENVOLVIDO POR:           ||")
        print("|| 1- hadrianus.lima.130@ufrn.edu.br     ||")
        print("||              LICENÇA MIT              ||")
        print("||  https://opensource.org/licenses/MIT  ||")
        print("\\\                                       //")
        print("  ---------------------------------------")
        input('APERTE ENTER PARA PROSSEGUIR')

print("PROGRAMA FECHADO")
