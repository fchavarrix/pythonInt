#Se debe llamar una libreria
from functools import reduce

def run():
    lista = [2,2,2,2,2]
    res = 1
    # for i in lista:
    #     res*= i
    res = reduce(lambda a,b: a*b, lista)

    print(f'La multiplicacion de todos los elementos es: {res}')



if __name__ == '__main__':
    run()