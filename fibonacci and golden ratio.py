
def fib(max):
    num = 1
    lista = [1]
    for i in range(1, max):
        lista.append(num)
        num = num + lista[i-1]
    return lista

lista_final = fib(2000)
numero = lista_final[len(lista_final)-1] / lista_final[len(lista_final)-2]
print(numero, len(lista_final))




