from zoom import ft_zoom
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    image = ft_load("animal.jpeg")
    print(image)
    cropped_image = ft_zoom(image)
    print(cropped_image)
    plt.imshow(cropped_image)
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    main()
