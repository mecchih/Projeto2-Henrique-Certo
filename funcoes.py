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