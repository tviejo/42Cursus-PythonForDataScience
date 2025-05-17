from abc import ABC, abstractmethod

class Character(ABC):
    """
    Character Class
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Character Constructor
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Character Method
        """
        pass

class Stark(Character):
    """
    Stark Class
    """

    def __init__(self, first_name, is_alive=True):
        """
        Stark Constructor
        """
        Character.__init__(self, first_name, is_alive)

    def die(self):
        """
        StarkMethod
        """
        self.is_alive = False
