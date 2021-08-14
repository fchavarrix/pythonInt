DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # all_pyhton_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_pyhton_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_pyhton_devs = list(map(lambda worker: worker['name'], all_pyhton_devs))

    # all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))

    # adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    # adults = list(map(lambda worker: worker['name'], adults))
    adults = [worker['name'] for worker in DATA if worker['age'] < 18]

    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)) #El simbolo | nos permite 
    # concatenar un diccionario con otro
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    

    for i in old_people:
        print(i)

    # for i in all_platzi_workers:
    #     print(i)

    # for i in adults:
    #     print(i)

    # for i in old_people:
    #     print(i)

if __name__ == '__main__':
    run()