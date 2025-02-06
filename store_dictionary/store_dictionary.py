import json

person = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

def write_dictonary(my_dictonary: dict, path_of_file: str):
    with open(path_of_file, 'w') as file:
        file.write(json.dumps(my_dictonary))


def read_dictonary(path_of_file: str):
    with open(path_of_file, 'r') as file:
        read_dict = json.load(file)
    
    print(type(read_dict))


write_dictonary(person, './person.txt')

read_dictonary('./person.txt')
