from typing import Any
import math

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistical measures based on input arguments.
    
    Args:
        *args: Variable number of numeric values
        **kwargs: Keyword arguments specifying which statistics to calculate
                 (mean, median, quartile, std, var)
    """
    if not args:
        print("ERROR")
        return

    # Convert args to list and sort for calculations
    numbers = sorted([float(x) for x in args])
    n = len(numbers)

    # Calculate statistics based on kwargs
    for key, value in kwargs.items():
        if value == "mean":
            mean = sum(numbers) / n
            print(f"mean : {mean}")
        elif value == "median":
            if n % 2 == 0:
                median = (numbers[n//2 - 1] + numbers[n//2]) / 2
            else:
                median = numbers[n//2]
            print(f"median : {median}")
        elif value == "quartile":
            q1_idx = int(n * 0.25)
            q3_idx = int(n * 0.75)
            q1 = numbers[q1_idx]
            q3 = numbers[q3_idx]
            print(f"quartile : [{q1}, {q3}]")
        elif value == "std":
            mean = sum(numbers) / n
            squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
            std = math.sqrt(squared_diff_sum / n)
            print(f"std : {std}")
        elif value == "var":
            mean = sum(numbers) / n
            squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
            var = squared_diff_sum / n
            print(f"var : {var}") 