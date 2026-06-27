def relatorios():
    import pickle
    from recup_dados import recuperar_clientes,recuperar_produtos,recuperar_vendas
    from validacoes import limpar_terminal

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
        print(" \  0- Voltar                      /")
        print("  --------------------------------")
        resp7 = input("Informe a opção desejada: ").strip()
        resp7_validas = ["0", "1", "2", "3", "4", "5"]
        while not (resp7 in resp7_validas):
            resp7 = input("Informe uma opção válida: ").strip()
        if resp7 == "0":
            break
        elif resp7 == "1":
            limpar_terminal()
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
        else:
            print()
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print(rosa_inicio+"|    FUNÇÃO EM DESENVOLVIMENTO⚠️   |"+rosa_final)
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
