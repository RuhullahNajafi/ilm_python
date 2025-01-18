from src.mdl.name import Name
from src.mdl.person import Person


def print_hi(name):
    person_1 = Person(Name("Max", "Muster"), 27)
    print(person_1)


if __name__ == '__main__':
    print_hi('PyCharm')

