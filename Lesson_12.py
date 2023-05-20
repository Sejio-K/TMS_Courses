'''
Написать класс-коллекцию (итератор) Zoo, в котором будет название зоопарка
и список животных (Animal с property - имя, тип (енот, тигр и тд),  возраст).
 У класса Zoo должны быть реализованы следующие методы:
- append (добавить животное)
- get (получить животное по id)
- get_by_type (получить животное по типу)
- delete - удалить животное из списка по id

По zoo мы должны уметь итерироваться и брать элемент по индексу,
 а также получать длину len(zoo) и уметь красиво выводить объект при
 приведении к строке (например, Зоопарк: имя зоопарка, n животных)

В классе Animal должны быть как минимум два classmethod, которые
 умеют создавать животное определенного типа с возрастом 0 и принимают в себя только имя, например:
- create_tiger(cls, name)

Для усложнения задачи можно добавить наследование и несколько типов животных на основе Animal

Дополнительно: написать class-decorator, который логгирует время работы функций класса в файл с именем функции и временем вызова
'''
class Animal:
    def __init__(self, animal_id, name, animal_type, age):
        self._id = animal_id
        self._name = name
        self._type = animal_type
        self._age = age

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def age(self):
        return self._age

    def __str__(self):
        return f"{self.name} ({self.type}), age {self.age}"

    @classmethod
    def create_enot(cls, name):
        return cls(None, name, "enot", 0)

    @classmethod
    def create_tigr(cls, name):
        return cls(None, name, "tigr", 0)


class Zoo:
    def __init__(self, name):
        self._name = name
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._animals):
            result = self._animals[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    @property
    def name(self):
        return self._name

    @property
    def animals(self):
        return self._animals


'''Дополнительно: написать class-decorator, который логгирует время работы функций класса в файл с именем функции и временем вызова '''

import datetime

def log_function_time(cls):
    class NewClass:
        def __init__(self, *args, **kwargs):
            self._wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            attribute = getattr(self._wrapped, name)
            if callable(attribute):
                def wrapper(*args, **kwargs):
                    start_time = datetime.datetime.now()
                    result = attribute(*args, **kwargs)
                    end_time = datetime.datetime.now()
                    log_entry = f"{name}_{start_time.strftime('%Y-%m-%d_%H-%M-%S')}: {end_time - start_time}\n"
                    with open(f"{name}.log", "a") as f:
                        f.write(log_entry)
                    return result
                return wrapper
            else:
                return attribute
    return NewClass


@log_function_time
class MyClass:
    def my_method(self):
        print("My method is called!")

obj = MyClass()
obj.my_method()