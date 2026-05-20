from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    "name": "Alice",
    "age": 30 # This will not raise a type error 
}

print(new_person)