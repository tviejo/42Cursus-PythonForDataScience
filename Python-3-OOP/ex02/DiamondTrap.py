from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """init method"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """set_eyes method"""
        self.eyes = color

    def set_hairs(self, color):
        """set_hairs method"""
        self.hairs = color

    def get_eyes(self):
        """get_eyes method"""
        return self.eyes
    
    def get_hairs(self):
        """get_hairs method"""
        return self.hairs