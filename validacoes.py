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
    try:
        datetime.strptime(data, "%d/%m/%Y")
        data = data.split("/")
        if int(data[2]) > datetime.now().year:
            return False
        elif int(data[2]) == datetime.now().year:
            if int(data[1]) > datetime.now().month:
                return False
            elif int(data[1]) == datetime.now().month:
                if int(data[0]) > datetime.now().day:
                    return False
        return True
    except:
        return False


def limpar_terminal():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def verificar_letras(letras):
    if letras.replace(" ","").isalpha():
        return True
    else:
        return False
    
def validar_fone(num):
    num = num.replace(" ","")
    num = num.replace("-","")
    num = num.replace("(","")
    num = num.replace(")","")
    tam = len(num)
    if tam != 11:
        return False
    if not num.isdigit():
        return False
    ddd = num[0]+num[1]
    ddd_validos = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "53", "54", "55", "61", "62", "63", "64", "65", "66", "67", "68", "69", "71", "73", "74", "75", "77", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
    if not (ddd in ddd_validos):
        return False
    if num[2] != "9":
        return False
    return True


def verificar_numeros(numeros):
    if numeros.isdigit():
        return True
    else:
        return False
    
def verificar_preco(valor):
    try:
        valor = float(valor)
        return True
    except:
        return False