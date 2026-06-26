def relatorios():
    from validacoes import limpar_terminal
    rosa_inicio = "\033[1;31;45m"
    rosa_final = "\033[m"
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
        else:
            print()
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print(rosa_inicio+"|    FUNÇÃO EM DESENVOLVIMENTO⚠️   |"+rosa_final)
            print(rosa_inicio+"-----------------------------------"+rosa_final)
            print()
            input("APERTE ENTER PARA PROSSEGUIR")
