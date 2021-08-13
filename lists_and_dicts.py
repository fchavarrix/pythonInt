def run():
    my_list = [1, 'Hi', True, 4.5]
    my_dict = {'firstName': "Luis", 'lastName': "Chavarri"}
    superList = [
        {'firstName': "Luis", 'lastName': "Chavarri"},
        {'firstName': "Cladia", 'lastName': "Fernandez"},
        {'firstName': "Catalina", 'lastName': "Chavarri"},
        {'firstName': "Paco", 'lastName': "Gutierrez"},
        {'firstName': "Alberto", 'lastName': "Rondon"},
    ]
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "float_nums": [1.43,2.55,3.12,4.54,5.98]

    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

if __name__ == '__main__':
    run()