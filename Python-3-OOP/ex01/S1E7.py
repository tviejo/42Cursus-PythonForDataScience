from S1E9 import Character

class Baratheon(Character):
    """Baratheon docstring"""
    def __init__(self, name, is_alive=True):
        Character.__init__(self, name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
    def __str__(self):
        """Baratheon str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Baratheon repr"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

class Lannister(Character):
    """Lannister docstring"""
    def __init__(self, name, is_alive=True):
        Character.__init__(self, name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
    def __str__(self):
        """Lannister str"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Lannister repr"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
    
    @classmethod
    def create_lannister(cls, name, is_alive=True):
        """Factory method"""
        return cls(name, is_alive)