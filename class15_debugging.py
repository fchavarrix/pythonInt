def divisores(num):
    divs = []
    for i in range(1,num+1):
        if num % i == 0:
            divs.append(i)
    return divs

# def divisores(num):
#     divs = [i for i in range(1,num+1) if num % i == 0]
#     return divs

def run():
    num = int(input('Ingresa un numero: '))
    print(divisores(num))
    print('Termino mi programa')

if __name__ == '__main__':
    run()