from src.mdl.name import Name
from src.mdl.person import Person, Sex


def main():
    bob = Person(Name("Bob", "Muster"), 27, Sex.MALE)
    alice = Person(Name("Alice", "Muster"), 25, Sex.FEMALE)
    bob.marry(alice)
    tom = bob.have_child(Name("Tom", "Muster"), Sex.MALE)
    eve = alice.have_child(Name("Eve", "Muster"), Sex.FEMALE)
    ben = bob.have_child(Name("Ben", "Muster"), Sex.MALE)
    anna = alice.have_child(Name("Anna", "Muster"), Sex.FEMALE)
    
    print()
    print(f"Spouse of {bob}: {bob.get_spouse()}")
    print(f"Spouse of {alice}: {alice.get_spouse()}")

    print()
    print(f"Children of {bob}: {bob.get_children()}")
    print(f"Children of {alice}: {alice.get_children()}")

    print()
    print(f"Parents of {tom}: {tom.get_parents()}")
    print(f"Parents of {eve}: {eve.get_parents()}")

    print()
    print(f"Father of {tom}: {tom.get_father()}")
    print(f"Mother of {tom}: {tom.get_mother()}")
    print(f"Father of {eve}: {eve.get_father()}")
    print(f"Mother of {eve}: {eve.get_mother()}")
    
    print()
    print(f"Siblings of {tom}: {tom.get_siblings()}")
    print(f"Siblings of {anna}: {anna.get_siblings()}")
    print(f"Brothers of {ben}: {ben.get_brothers()}")
    print(f"Sisters of {tom}: {tom.get_sisters()}")

    ben.set_age(30)
    nicole = Person(Name("Nicole", "Bauer"), 28, Sex.FEMALE)
    ben.marry(nicole)
    tim = ben.have_child(Name("Tim", "Muster"), Sex.MALE)

    print()
    print(f"Parents of {tim}: {tim.get_parents()}")
    print(f"Grandparents of {tim}: {tim.get_grandparents()}")
    print(f"Grandchildren of {bob}: {bob.get_grandchildren()}")
    print(f"Grandchildren of {alice}: {alice.get_grandchildren()}")


if __name__ == '__main__':
    main()