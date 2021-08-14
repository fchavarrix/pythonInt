def run():
    lista = [1,2,3,4,5]
    #pares = [i for i in lista if i%2 !=0]
     
    pares = list(filter(lambda x: x%2 != 0, lista))
    print(pares)

if __name__ == '__main__':
    run()