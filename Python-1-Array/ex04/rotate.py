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
    rows = len(imageList)
    cols = len(imageList[0])
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = image_array[i][j]

    transposed = np.array(transposed)
    print("New shape after Transpose:", transposed.shape)
    return transposed.tolist()
