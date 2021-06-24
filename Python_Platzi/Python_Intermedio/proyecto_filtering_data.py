DATA = [
    {
        'name': 'Facundo',
        'age': 12,
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
        'age': 90,
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
        'age': 82,
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

def main():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"] #With list comprehension
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"] #With list comprehension

    adults = list(filter(lambda worker: worker["age"] > 18, DATA)) #With filter list / high order functions
    adults = list(map(lambda worker: worker["name"], adults)) #With filter list / high order functions

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # Challenge: 
    # 1- Create the lists all_python_devs and all_Platzi_workers using a combination of filter map.
    # 2- Create the lists old_people and adults using list comprehensions.
    
    #Part 1
    all_python_devs_2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_2 = list(map(lambda worker: worker["name"], all_python_devs_2))

    #Part 2 - a
    old_people_2 = [worker | {"old": worker["age"] > 70} for worker in DATA if worker["age"] > 70]
    old_people_2 = [worker["name"] for worker in old_people_2 if worker["old"] == True]

    #Part 2 - b
    adults_2 = [worker["name"] for worker in DATA if worker["age"] > 18 ]


    print(adults_2)

if __name__ == "__main__":
    main()