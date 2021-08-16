
# try:
#     f = open('archivo.txt')
#     # hacer cualquier cosa con nuestro archivo
# finally:
#     f.close()

#########################################################################################
## Se atrapa el error cuando se deja la cadena vacia y tambien cuando es un error de tipo
#########################################################################################
def palindrome(s):
    try:
        if len(s) == 0:
            raise ValueError('No se puede ingresar una cadena vacía')
        return s == s[::-1]
    except ValueError as ve:
        print(ve)
        return False

try:
    print(palindrome(''))
except TypeError:
    print('Solo se pueden ingresar strings')

###################################################################################
## Prueba cuando se evalua con un tipo diferente al esperado y cuando se deja vacio
###################################################################################
# def palindrome(s):
#     return s == s[::-1]

# try:
#     # print(palindrome(1)) #se imprime el mensaje ya que se produce la excepcion del TypeError
#     print(palindrome('')) #se imprime la cadena vacia por lo que python devuelve True
# except TypeError:
#     print('Solo se pueden ingresar strings') 

# def palindrome(s):
#     return s == s[::-1]
# print(palindrome(1))

"""
Traceback (most recent call last):
  File "/home/atlas/pythonIntermediate/pythonInt/class16_exceptionsHandling.py", line 4, in <module>
    print(palindrome(1))
  File "/home/atlas/pythonIntermediate/pythonInt/class16_exceptionsHandling.py", line 2, in palindrome
    return s == s[::-1]
TypeError: 'int' object is not subscriptable
"""

# def palindrome(s):
#     return s == s[::-1]

# def run():
#     print(palindrome(1))

# if __name__ == '__main__':
#     run()


#try, except, finally and raise