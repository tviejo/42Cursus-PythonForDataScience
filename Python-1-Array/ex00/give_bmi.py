import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the BMI of a person.

    Parameters:
    height (list[int | float]): List of heights in meters.
    weight (list[int | float]): List of weights in kilograms.

    Returns:
    list[int | float]: List of calculated BMI values.
    """
    return (np.array(weight) / (np.array(height) ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a BMI.

    Parameters:
    bmi (list[int | float]): List of BMI values.
    limit (int): Limit for BMI.

    Returns:
    list[bool]: List indicating whether each BMI exceeds the limit.
    """
    return (np.array(bmi) > limit).tolist()
