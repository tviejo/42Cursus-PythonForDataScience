import numpy as np


def ft_invert(array: list) -> list:
    """
    Invert an image.
    """

    if not isinstance(array, list):
        return None
    if not all(isinstance(row, list) for row in array):
        return None
    if not all(len(row) == len(array[0]) for row in array):
        return None

    image_array = np.array(array)
    inverted_image = 255 - image_array
    return inverted_image.tolist()


def ft_red(array: list) -> list:
    """
    Red filter an image.
    """

    if not isinstance(array, list):
        return None
    if not all(isinstance(row, list) for row in array):
        return None
    if not all(len(row) == len(array[0]) for row in array):
        return None

    image_array = np.array(array)
    image_array[:, :, 1] = 0
    image_array[:, :, 2] = 0
    return image_array.tolist()


def ft_blue(array: list) -> list:
    """
    Blue filter an image.
    """

    if not isinstance(array, list):
        return None
    if not all(isinstance(row, list) for row in array):
        return None
    if not all(len(row) == len(array[0]) for row in array):
        return None

    image_array = np.array(array)
    image_array[:, :, 0] = 0
    image_array[:, :, 1] = 0
    return image_array.tolist()


def ft_green(array: list) -> list:
    """
    Green filter an image.
    """

    if not isinstance(array, list):
        return None
    if not all(isinstance(row, list) for row in array):
        return None
    if not all(len(row) == len(array[0]) for row in array):
        return None

    image_array = np.array(array)
    image_array[:, :, 0] = 0
    image_array[:, :, 2] = 0
    return image_array.tolist()


def ft_grey(array: list) -> list:
    """
    Grey filter an image.
    """

    if not isinstance(array, list):
        return None
    if not all(isinstance(row, list) for row in array):
        return None
    if not all(len(row) == len(array[0]) for row in array):
        return None

    image_array = np.array(array)
    for i in range(len(image_array)):
        for j in range(len(image_array[0])):
            grey = sum(image_array[i][j]) // 3
            image_array[i][j] = [grey, grey, grey]
    return image_array.tolist()
