def recuperar_clientes():
    import pickle
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

def recuperar_produtos():
    import pickle
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

def recuperar_vendas():
    import pickle
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