from typing import Any, Callable

def callLimit(limit: int):
    """
    Decorator that limits the number of times a function can be called.
    
    Args:
        limit: Maximum number of times the function can be called
    
    Returns:
        A decorator function that enforces the call limit
    """
    count = 0
    
    def callLimiter(function: Callable):
        """
        Inner decorator that tracks function calls.
        
        Args:
            function: The function to be called
        
        Returns:
            A wrapper function that enforces the call limit
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper function that checks the call limit before executing.
            
            Args:
                *args: Variable length argument list
                **kwds: Arbitrary keyword arguments
            
            Returns:
                The result of the function call if within limit
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        
        return limit_function
    
    return callLimiter 