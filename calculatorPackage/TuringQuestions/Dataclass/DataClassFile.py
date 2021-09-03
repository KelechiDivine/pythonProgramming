from dataclasses import dataclass

@dataclass

class Person:

    name: str
    age:int
    
    
person = Person("John", age=41)
print(person.name)

print(person.age)

print(Person)