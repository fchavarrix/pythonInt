# def palindrome(s):
#     try:
#         if len(s) == 0:
#             raise ValueError('No se puede ingresar una cadena vacía')
#         return s == s[::-1]
#     except ValueError as ve:
#         print(ve)
#         return False

def divisores(num):
    try:
        if num <0:
            raise ValueError('No se puede ingresar un número negativo')
        divs = []
        for i in range(1,num+1):
            if num % i == 0:
                divs.append(i)
        return divs
    except ValueError as ve:
        print(ve)
        return False

# def divisores(num):
#     divs = [i for i in range(1,num+1) if num % i == 0]
#     return divs

def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisores(num))
        print('Termino mi programa')
    except ValueError:
        print('Debes ingresar un número natural')

if __name__ == '__main__':
    run()