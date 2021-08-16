def palindrome(s):
    assert len(s) > 0, 'No se puede ingresar una cadena vacia'
    return s == s[::-1]

print(palindrome(''))



# def divisores(num):
#     divs = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             divs.append(i)
#     return divs

# def run():
#     num = input('Ingresa un numero: ')
#     assert num.isnumeric(), 'Debes ingresar un número'
#     print(divisores(int(num)))
#     print('Termino mi programa')

# if __name__ == '__main__':
#     run()