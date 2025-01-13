from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    """
    Main function.
    """

    image = ft_load("landscape.jpg")
    plt.imshow(image)
    plt.axis("on")
    # plt.show()
    plt.savefig("image.jpg")  # for wsl
    inverted_image = ft_invert(image)
    plt.imshow(inverted_image)
    plt.axis("on")
    # plt.show()
    plt.savefig("inverted_image.jpg")  # for wsl
    red_image = ft_red(image)
    plt.imshow(red_image)
    plt.axis("on")
    # plt.show()
    plt.savefig("red_image.jpg")  # for wsl
    green_image = ft_green(image)
    plt.imshow(green_image)
    plt.axis("on")
    # plt.show()
    plt.savefig("green_image.jpg")  # for wsl
    blue_image = ft_blue(image)
    plt.imshow(blue_image)
    plt.axis("on")
    # plt.show()
    plt.savefig("blue_image.jpg")  # for wsl
    grey_image = ft_grey(image)
    plt.imshow(grey_image)
    plt.axis("on")
    # plt.show()
    plt.savefig("grey_image.jpg")  # for wsl


if __name__ == "__main__":
    main()
