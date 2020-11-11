"""
Author: Omer Oz
Date: 14/9/2020
Description: a circle class
"""
from Shape import Shape


class Circle(Shape):

    def __init__(self, color, r):
        """
        Constructor
        :param color: the color from the superclass
        :param r: the radius of the circle
        """
        super().__init__(color)
        self.r = r

    def get_area(self):
        """
        :return: the area of the circle
        """
        return 3.14 * self.r * self.r

    def get_per(self):
        """
        :return: the peremiter of the circle
        """
        return 2 * 3.14 * self.r


def main():
    pass


"""
checking with assert
"""
if __name__ == '__main__':
    c = Circle("Yellow", 2)
    assert c.get_per() == 12.56
    main()
