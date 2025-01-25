from enum import Enum
from src.mdl.name import Name


class Sex(Enum):
    FEMALE = 1
    MALE = 2

    def __str__(self):
        return self.name.lower()


class Person:

    def __init__(self, name: Name, age: int, sex: Sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"{self.name} (age: {self.age}, sex: {self.sex})"
