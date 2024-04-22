
def fib(max):
    number = 1
    list = [1]
    for i in range(1, max):
        list.append(number)
        number = number + lista[i-1]
    return list

finalList = fib(2000)
number = finalList[len(finalList)-1] / finalList[len(finalList)-2]
print(number, len(finalList))




