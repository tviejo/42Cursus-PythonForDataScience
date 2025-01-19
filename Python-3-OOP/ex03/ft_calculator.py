class calculator:
    def __init__(self, values) -> None:
        """init class"""
        self.values = values


    def __add__(self, scalar) -> None:
        """add method"""
        self.values = [x + scalar for x in self.values]
        print(self.values)
    

    def __mul__(self, scalar) -> None:
        """mul method"""
        self.values = [x * scalar for x in self.values]
        print(self.values)


    def __sub__(self, scalar) -> None:
        """sub method"""
        self.values = [x - scalar for x in self.values]
        print(self.values)


    def __truediv__(self, scalar) -> None:
        """truediv method"""
        if scalar == 0:
            raise ZeroDivisionError
        self.values = [x / scalar for x in self.values]
        print(self.values)