

class Name:

    def __init__(self, first_name, last_name):

        # Check if the arguments are of the correct type
        if not isinstance(first_name, str):
            raise TypeError(f"Expected 'first_name' to be of type 'str', but got '{type(first_name).__name__}'")
        if not isinstance(last_name, str):
            raise TypeError(f"Expected 'last_name' to be of type 'str', but got '{type(last_name).__name__}'")
        
        # Check if the arguments are of the correct value
        if not first_name:
            raise ValueError(f"Expected 'first_name' to be a non-empty string, but got '{first_name}'")
        if not last_name:
            raise ValueError(f"Expected 'last_name' to be a non-empty string, but got '{last_name}'")
        
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    def __eq__(self, other: 'Name') -> bool:
        if not isinstance(other, Name):
            return NotImplemented
        return self.first_name == other.first_name and self.last_name == other.last_name