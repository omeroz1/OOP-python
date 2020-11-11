from Shape import Shape

"""
Author: Omer Oz
Date: 14/9/2020
Description: an abstract quad class
"""


class Quad(Shape):

    def __init__(self, color, x, y):
        """
        Constructor
        :param color: the color from the super
        :param x: length
        :param y: width
        """
        super().__init__(color)
        self.x = x
        self.y = y

    def get_area(self):
        """
        :return: the area of the Quad
        """
        return self.x * self.y

    def get_per(self):
        """
        :return: the peremiter of the Quad
        """
        return 2 * self.x + 2 * self.y

    @staticmethod
    def add_quad(s1, s2):
        """
        Create a new shape from two different quads with the correct area and peremiter
        :param s1: first shape
        :param s2: second shape
        :return: the new shape
        """
        if s1.color == s2.color and s1.x == s2.x or s1.x == s1.y or s1.y == s2.x or s1.y == s1.y:
            if s1.x == s2.x:
                return Square(s1.x, s2.x)
            if s1.x == s2.y:
                return Rectangle(s1.x, s2.y)
            if s1.y == s2.x:
                return Rectangle(s1.y, s2.x)
            if s1.y == s2.y:
                return Square(s1.y, s2.y)
        return "cannot convert"


class Square(Quad):

    def __init__(self, color, x):
        """
        Constructor
        :param color: color from the superclass
        :param x: the length and width
        """
        super().__init__(color, x, x)


class Rectangle(Quad):

    def __init__(self, color, x, y):
        """
        Constructor
        :param color: color from the superclass
        :param x: the length
        :param y: the width
        """
        super().__init__(color, x, y)


def main():
    pass


"""
checking with assert
"""
if __name__ == '__main__':
    a = Square("Yellow", 5)
    b = Rectangle("red", 3, 2)
    assert a.get_area() == 25
    assert b.get_color() == "red"
    main()
