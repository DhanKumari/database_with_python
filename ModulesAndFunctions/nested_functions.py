def greet_pythons(items:list)-> None:

    greeting="hello"

    def make_greeting(item:str)-> str:
        greeting="hii"
        return f'{greeting} {item}'
    
    for item in items:
        print(make_greeting(item))
    print(f'inside greet_python its value is {greeting}')

name =  ['john','Eric','Graham','Terry','Terry','Michael']

greet_pythons(name)