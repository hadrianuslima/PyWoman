from validacoes import validar_cpf , validar_data , verificar_preco , verificar_letras , verificar_numeros , limpar_terminal, validar_fone
from modulo_clientes import CRUD_cliente
from modulo_produtos import CRUD_produto
from modulo_vendas import CRUD_vendas
from modulo_relatorios import relatorios
from info_sistem import sobre_sistm

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
    print("||  0- Sair🔙                 //")
    print("  ---------------------------")
    modulo = input("Informe o módulo que deseja acessar: ").strip()
    modulos_validos = ["0", "1", "2", "3", "4", "5"]
    while not (modulo in modulos_validos):
        modulo = input("Informe uma opção válida: ").strip()
    if modulo == "1":
        CRUD_cliente()
    elif modulo == "2":
        CRUD_produto()
    elif modulo == "3":
        CRUD_vendas()
    elif modulo == "4":
        relatorios()
    elif modulo == "5":
        sobre_sistm()
print("PROGRAMA FECHADO")