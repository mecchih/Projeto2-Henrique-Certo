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