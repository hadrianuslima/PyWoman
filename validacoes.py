def validar_cpf(cpf):
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0
    if tam != 11:
        return False
    for i in range(11):
        if (cpf[i]<'0')or(cpf[i]>'9'):
            return False
    for i in range(9):
        soma += (int(cpf[i])*(10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += (int(cpf[i])*(11-i))
    d2 = 11 - (soma%11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False
    return True

def validar_data(data):
    from datetime import datetime  # Valida de data usando a biblioteca datetime
    loop = "1"
    while loop == "1":
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except:
            data = input("Informe a data correta no formato DD/MM/AAAA: ").strip()

def limpar_terminal():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def verificar_letras(letras):
    while not letras.replace(" ", "").isalpha():
        letras = input("APENAS LETRAS: ").strip()
    return letras

def verificar_numeros(numeros):
    while not numeros.isdigit():
        numeros = input("APENAS NÚMEROS: ").strip()
    return numeros

def verificar_preco(valor):
    loop = True
    while loop == True:
        try:
            valor = float(valor)
            return valor
            loop = False
        except ValueError:
            valor = input("INFORME O VALOR DE FORMA CORRETA: R$").strip()