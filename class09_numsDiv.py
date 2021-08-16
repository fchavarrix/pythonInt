def run():
    print('Aqui empieza')
    listCompr1 = [i for i in range(1,100000) if i % 36 == 0]
    print(listCompr1)

if __name__ == '__main__':
    run()