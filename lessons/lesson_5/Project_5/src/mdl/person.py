from src.mdl.name import Name


class Person:

    def __init__(self, name: Name, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age: {self.age})"
