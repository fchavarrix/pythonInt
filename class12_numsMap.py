def run():
    lista = [1,2,3,4,5]
    # squares = [i*2 for i in lista]
    # 
    squares = list(map(lambda x: x**2, lista))
    print(squares)

if __name__ == '__main__':
    run()