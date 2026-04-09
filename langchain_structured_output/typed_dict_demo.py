from typing import TypedDict # Does not validate data type but helps in overall type hint

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name':'Tushar', 'age':35}
print(new_person)