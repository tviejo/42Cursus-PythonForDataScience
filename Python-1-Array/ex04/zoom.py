import numpy as np


def ft_zoom(imageList: list) -> list:
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
    cropped_image = image_array[200:600, 400:800]
    print("New shape after slicing:", cropped_image.shape)
    return cropped_image.tolist()
