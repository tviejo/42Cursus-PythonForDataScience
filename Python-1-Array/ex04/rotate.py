import numpy as np


def ft_rotate(imageList: list) -> list:
    """
    Zoom an image.
    """

    if not isinstance(imageList, list):
        return None
    if not all(isinstance(row, list) for row in imageList):
        return None
    if not all(len(row) == len(imageList[0]) for row in imageList):
        return None

    image_array = np.array(imageList)
    rotated_image = np.rot90(image_array)
    print("New shape after Transpose:", rotated_image.shape)
    return rotated_image.tolist()
