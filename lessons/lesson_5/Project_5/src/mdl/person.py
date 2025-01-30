from enum import Enum
from src.mdl.name import Name


class Sex(Enum):
    FEMALE = 1
    MALE = 2

    def __str__(self):
        return self._name.lower()


class Person:

    AGE_OF_MAJORITY = 18


    def __init__(self, name: Name, age: int, sex: Sex):

        # Check if the arguments are of the correct type
        if not isinstance(name, Name):
            raise TypeError(f"Expected 'name' to be of type 'Name', but got '{type(name).__name__}'")
        if not isinstance(age, int):
            raise TypeError(f"Expected 'age' to be of type 'int', but got '{type(age).__name__}'")
        if not isinstance(sex, Sex):
            raise TypeError(f"Expected 'sex' to be of type 'Sex', but got '{type(sex).__name__}'")
        
        # Check if the arguments are of the correct value
        if age < 0:
            raise ValueError(f"Expected 'age' to be greater or equal to 0, but got '{age}'")
        if sex not in Sex:
            raise ValueError(f"Expected 'sex' to be a valid instance of 'Sex', but got '{sex}'")
        
        # Set the attributes of the person
        self._name = name
        self._age = age
        self._sex = sex

        self._alive = True
        self._spouse = None
        self._children = []
        self._parents = []
        # The attribute names starting with an underscore are meant to be private

    
    def __str__(self):
        return f"{self._name}{' -DEAD-' if not self._alive else ''}"
    

    def __repr__(self):
        return f"{self._name}{' -DEAD-' if not self._alive else ''}"
    

    def marry(self, person: 'Person') -> None:
        # Check if the argument is of the correct type
        if not isinstance(person, Person):
            raise TypeError(f"Expected 'person' to be of type 'Person', but got '{type(person).__name__}'")
        # Check if both persons are alive
        if not self._alive or not person._alive:
            raise PermissionError("Both persons must be alive to marry")
        # Check if both persons are of legal age
        if not self.is_adult() or not person.is_adult():
            raise PermissionError("Both persons must be of legal age to marry")
        # Check if both persons are of different gender
        if self._sex == person._sex:
            raise PermissionError("Persons of the same sex cannot marry")
        # Check if both persons are single
        if self._spouse is not None or person._spouse is not None:
            raise PermissionError("Both persons must be single to marry")
        # Check if the persons are not the same
        if self == person:
            raise PermissionError("Persons cannot marry themselves")
        
        # Set the spouse of each person to the other person
        self._spouse = person
        person._spouse = self

    
    def divorce(self) -> None:
        # Check if the person is married
        if self._spouse is None:
            raise ValueError("Person is not married, so cannot divorce")
        
        self._spouse._spouse = None
        self._spouse = None

    
    def have_child(self, name: Name, sex: Sex) -> 'Person':
        # Check if the argument is of the correct type
        if not isinstance(name, Name):
            raise TypeError(f"Expected 'name' to be of type 'Name', but got '{type(name).__name__}'")
        
        # Check if the person is married
        if self._spouse is None:
            raise PermissionError("Person must be married to have a child")
        
        # Check if the person already has a child with the given name
        if any(child._name == name for child in self._children):
            raise PermissionError(f"Person already has a child with the given name {name}")
        
        # Check if the person and the spouse are alive
        if not self._alive or not self._spouse._alive:
            raise PermissionError("Both parents must be alive to have a child")
        
        # Create a new child with the given name and sex and an age of 0
        child = Person(name, 0, sex)

        # Add the child to the parents' and spouse's children lists
        self._children.append(child)
        self._spouse._children.append(child)

        # Add self and the spouse to the child's parents
        child._parents.extend([self, self._spouse])

        return child
    

    def die(self) -> None:
        # Check if the person is already dead
        if not self._alive:
            raise PermissionError("Person is already dead")

        # Set the person to dead
        self._alive = False


    def is_adult(self) -> bool:
        # Return whether the person is of legal age
        return self._age >= Person.AGE_OF_MAJORITY
    

    def is_alive(self) -> bool:
        # Return whether the person is alive
        return self._alive
    

    def is_married(self) -> bool:
        # Return whether the person is married
        return self._spouse is not None
    

    def is_single(self) -> bool:
        # Return whether the person is single
        return self._spouse is None
    

    def is_parent(self) -> bool:
        # Return whether the person has children
        return bool(self._children)
    

    def is_grandparent(self) -> bool:
        # Return whether the person has grandchildren
        return any(child._children for child in self._children)
    
    
    def get_spouse(self) -> 'Person':
        # Return the spouse of the person
        return self._spouse
    

    def get_children(self) -> list['Person']:
        # Return the children of the person
        return self._children
    

    def get_parents(self) -> list['Person']:
        # Return the parents of the person
        return self._parents


    def get_father(self) -> 'Person':
        # Return the male parent if it exists, otherwise return None
        return next((parent for parent in self._parents if parent._sex == Sex.MALE), None)
    

    def get_mother(self) -> 'Person':
        # Return the female parent if it exists, otherwise return None
        return next((parent for parent in self._parents if parent._sex == Sex.FEMALE), None)


    def get_siblings(self) -> list['Person']:
        # Create an empty list to store the siblings
        siblings = []
        if self._parents:
            # Iterate over both parents
            for parent in self._parents:
                # Iterate over the children of each parent
                for sibling in parent.get_children():
                    # Check if the sibling is not the person itself and not 
                    # already in the list of siblings (to avoid duplicates)
                    if sibling != self and sibling not in siblings:
                        # Add the sibling to the list of siblings
                        siblings.append(sibling)
        return siblings
    

    def get_brothers(self) -> list['Person']:
        # Return the brothers of the person (siblings that are MALE)
        return [sibling for sibling in self.get_siblings() if sibling._sex == Sex.MALE]
    

    def get_sisters(self) -> list['Person']:
        # Return the sisters of the person (siblings that are FEMALE)
        return [sibling for sibling in self.get_siblings() if sibling._sex == Sex.FEMALE]
    

    def get_grandparents(self) -> list['Person']:
        # Return the grandparents of the person
        return [grand_parent for parent in self._parents for grand_parent in parent.get_parents()]
        # Alternative solution:
        # grandparents = []
        # if self._parents:
        #     # Iterate over both parents
        #     for parent in self._parents:
        #         # Add the parents of each parent to the list of grandparents
        #         grandparents.extend(parent.get_parents())
        # return grandparents
    
    
    def get_grandchildren(self) -> list['Person']:
        # Return the grandchildren of the person
        return [grand_child for child in self._children for grand_child in child.get_children()]
        # Alternative solution:
        # grandchildren = []
        # if self._children:
        #     # Iterate over the children of the person
        #     for child in self._children:
        #         # Add the children of each child to the list of grandchildren
        #         grandchildren.extend(child.get_children())
        # return grandchildren

    
    def set_age(self, age: int) -> None:
        # Check if the argument is of the correct type
        if not isinstance(age, int):
            raise TypeError(f"Expected 'age' to be of type 'int', but got '{type(age).__name__}'")
        # Check if the argument is of the correct value
        if age < 0:
            raise ValueError(f"Expected 'age' to be greater or equal to 0, but got '{age}'")
        # Check if the person is alive
        if not self._alive:
            raise PermissionError("Person is dead, so cannot change age")
        
        self._age = age
