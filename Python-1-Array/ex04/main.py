from load_image import ft_load
from rotate import ft_rotate
from zoom import ft_zoom
import matplotlib.pyplot as plt


def main():
    """
    Main function.
    """

    image = ft_load("animal.jpeg")
    print(image)
    cropped_image = ft_zoom(image)
    print(cropped_image)
    rotated_image = ft_rotate(cropped_image)
    print(rotated_image)
    plt.imshow(rotated_image)
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    main()
