'''Задача 1. Создать родительский класс машина, у которого есть атрибуты model,
age, color и weight, из них обязательный только  model. Также у класса должны
быть методы move, stop,  birthday, методы move и stop выводят сообщение на
экран "move", "stop", а birthday увеличивает атрибут age на 1. Если атрибут age =
None, то выбрасывает исключение с сообщением "атрибут age не задан". '''


class Car:
    def __init__(self, model, age = None, color = None, weight = None):
        self.model = model
        self.age = age
        self.color = color
        self.weight = weight
    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        if self.age is None:
            raise ValueError("атрибут age не задан")
        self.age += 1

'''Есть csv файл со списком людей, нужно прочитать его и преобразовать
в список датаклассов. То есть нужно создать датакласс с атрибутами name, age,
при этом тип age : Optional[int]. У датакласса должно быть property birth_year,
которое считает возраст'''
import csv
from dataclasses import dataclass

from dataclasses import dataclass
from typing import Optional

import csv
@dataclass
class Person:
    name: str
    age: Optional[int]

    @property
    def birth_year(self):
        return 2023 - self.age

people = []
with open('names.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name, age = row
        age = int(age) if age else None
        person = Person(name, age)
        people.append(person)

for person in people:
    print(f"Name: {person.name}, Age: {person.age}, Birth Year: {person.birth_year}")


'''Задача 4*. Доработать созданный на уроке класс Family следующим образом:
создать методы, которые умеют возвращать детей по роли в семье (список
FamilyMember), а также мать, отца и домашних животных
доработать класс FamilyMember таким образом, чтобы у члена семьи могли
быть mother и  father - тоже экземпляры FamilyMember, эти атрибуты
опциональны, то есть у человека может отсутствовать mother и father
добавить метод print_family_tree, который будет выводить семейное древо
(формат вывода неважен):'''

class Family:

    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def __len__(self):
        return len(self.members)

    def add_family_member(self, member):
        self.members.append(member)

    def __str__(self):
        return f"Family: last_name - {self.last_name}, count - {len(self.members)}"

    def get_children_by_role(self, role):
        children = []
        for member in self.members:
            if member.role == role and member.age is not None and member.age < 18:
                children.append(member)
        return children

    def get_mother(self):
        for member in self.members:
            if member.role == "mother":
                return member
        return None

    def get_father(self):
        for member in self.members:
            if member.role == "father":
                return member
        return None

    def get_pets(self):
        pets = []
        for member in self.members:
            if member.role == "pet":
                pets.append(member)
        return pets


class FamilyMember:

    def __init__(self, name, role=None, age=None):
        self.name = name
        self.role = role
        self.age = age

    def __str__(self):
        return f"FamilyMember: {self.name}, role: {self.role}"


son = FamilyMember(name="Roma", role="son")
father = FamilyMember(name="Nikita", role="father", age=43)

members = [son, father]
family = Family(last_name="Гаврильчик", members=members)
print(f"Count {len(family)}")
# len(family)