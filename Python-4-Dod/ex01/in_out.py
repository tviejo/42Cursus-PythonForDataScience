from typing import Callable, Any

def square(x: int | float) -> int | float:
    """
    Calculate the square of a number.
    
    Args:
        x: A number (int or float)
    
    Returns:
        The square of the input number
    """
    return x * x

def pow(x: int | float) -> int | float:
    """
    Calculate the number raised to its own power.
    
    Args:
        x: A number (int or float)
    
    Returns:
        The number raised to its own power
    """
    return x ** x

def outer(x: int | float, function: Callable) -> object:
    """
    Create a closure that maintains a counter and applies the given function.
    
    Args:
        x: Initial value (int or float)
        function: Function to apply (square or pow)
    
    Returns:
        A closure that when called returns the result of applying the function
    """
    count = 0
    current = x
    
    def inner() -> float:
        """
        Inner function that maintains state and applies the function.
        
        Returns:
            Result of applying the function to the current value
        """
        nonlocal count, current
        if count == 0:
            count += 1
            current = function(current)
            return current
        current = function(current)
        count += 1
        return current
    
    return inner 