import random
def rolar_dados(numero):
    lista = []
    i =0
    while i < numero:
        valor = random.randint(1,6)
        lista.append(valor)
        i+=1
    return lista

def guardar_dado(rolados,guardados,numero):

    guardados.append(rolados[numero])
    del rolados[numero]
    return [rolados,guardados]

def remover_dado(rolados,guardados,numero):
    rolados.append(guardados[numero])
    del guardados[numero]
    return [rolados,guardados]

 
def calcula_pontos_regra_simples(lista_inteiros):
    dicionario = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in lista_inteiros:
        if i in dicionario:
            dicionario[i] += i

    return dicionario

def calcula_pontos_soma(lista_inteiros):
    soma = 0
    for i in lista_inteiros:
        soma += i
    return soma

def calcula_pontos_sequencia_baixa(lista_inteiros):
    if 1 in lista_inteiros and 2 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros or  5 in lista_inteiros and 2 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros or 6 in lista_inteiros and 5 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros:
        return 15
    else:
        return 0 
    
def calcula_pontos_sequencia_alta(lista_inteiros):
    if 1 in lista_inteiros and 2 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros and 5 in lista_inteiros or 2 in lista_inteiros and 3 in lista_inteiros and 4 in lista_inteiros and 5 in lista_inteiros and 6 in lista_inteiros:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(lista_inteiros):
    numeros = []
    for numero in lista_inteiros:
        if numero in numeros:
            continue
        else:
            numeros.append(numero)
    if len(numeros) != 2:
        return 0
    else:
        soma = 0
        for i in lista_inteiros:
            soma += i
    return soma
            
def calcula_pontos_quadra(lista_inteiros):
    quadra = []
    for numero in lista_inteiros:
        contagem = 0
        for i in range(len(lista_inteiros)):
            if lista_inteiros[i] == numero:
                contagem += 1
        if contagem >= 4:
            quadra.append(numero)
    if len(quadra) == 0:
        return 0
    else:
        soma = 0
        for i in lista_inteiros:
            soma += i
    return soma
    
def calcula_pontos_quina(lista_inteiros):
    tem = False
    for numero in lista_inteiros:
        if tem == True:
            break
        contagem = 0
        for i in range(len(lista_inteiros)):
            if lista_inteiros[i] == numero:
                contagem +=1
            if contagem >= 5:
                tem = True
    if tem == True:
        return 50
    else:
        return 0         
    
            

    