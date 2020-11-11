"""
Author: Omer Oz
Date: 14/9/2020
Description: an abstract shape class
"""


class Shape(object):

    def __init__(self, color):
        """
        Constructor
        :param color: create a color for the shape
        """
        self.color = color

    def set_color(self, color):
        """
        :param color: sets a given color
        """
        self.color = color

    def get_color(self):
        """
        :return: the color
        """
        return self.color

    def get_area(self):
        """
        :return: the area
        """
        pass

    def get_per(self):
        """
        :return: the perimeter
        """
        pass


def main():
    pass


"""
checking with assert
"""
if __name__ == '__main__':
    s = Shape("Yellow")
    assert s.get_color() == "Yellow"
    main()
