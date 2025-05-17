import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """
    Generate a random 15-character string using lowercase letters.
    
    Returns:
        A random 15-character string
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))

@dataclass
class Student:
    """
    A dataclass representing a student with name, surname, and generated attributes.
    
    Attributes:
        name: Student's first name
        surname: Student's last name
        active: Whether the student is active (default: True)
        login: Generated login based on surname
        id: Generated random ID
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)
    
    def __post_init__(self):
        """
        Initialize the login and id fields after the main initialization.
        Login is the capitalized surname, and id is a random 15-character string.
        """
        self.login = self.surname.capitalize()
        self.id = generate_id() 