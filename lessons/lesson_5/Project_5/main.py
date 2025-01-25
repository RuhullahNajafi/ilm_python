from src.mdl.name import Name
from src.mdl.person import Person, Sex


def main(name):
    person_1 = Person(Name("Max", "Muster"), 27, Sex.MALE)
    print(person_1)


if __name__ == '__main__':
    main('PyCharm')