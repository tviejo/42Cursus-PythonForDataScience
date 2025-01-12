import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """
    Load an image from a file.
    """

    try:
        image = Image.open(path)
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None

    try:
        image = image.convert("RGB")
    except ValueError:
        print("Error: Image is not RGB.")
        return None

    width, height = image.size

    print("the shape of image is:", np.shape(image))
    pixels = np.array(image)

    return pixels.tolist()
