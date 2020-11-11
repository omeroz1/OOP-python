"""
Author: Omer Oz
Date: 14/9/2020
Description: Class of shapes (Square, Rectangle, Circle)
"""
import random
from Circle import Circle
from Quad import Square, Rectangle
from Shape import Shape

COLORS = ["red", "green", "blue"]


class MyContainer(Shape):

    def __init__(self):
        """
        Constructor
        creates a list of objects
        """
        self.my_objects = []

    def generate(self, x):
        """
        :param x: the amount of shapes to create
        puts all the shapes in the list
        """
        for y in range(x):
            z = random.randint(0, 2)
            r = random.randint(0, 10)
            length = random.randint(0, 10)
            width = random.randint(0, 10)

            if z == 0:
                Square(COLORS[0], length)
                self.my_objects.append(Square(COLORS[0], length))
            if z == 1:
                Rectangle(COLORS[1], x, y)
                self.my_objects.append(Rectangle(COLORS[1], length, width))
            if z == 2:
                Circle(COLORS[2], r)
                self.my_objects.append(Circle(COLORS[2], r))

    def sum_areas(self):
        """
        :return: the sum of the areas from of all the shapes
        """
        sum = 0
        for obj in self.my_objects:
            sum += obj.get_area()
        return sum

    def sum_peremiters(self):
        """
        :return: the sum of the peremiters from of all the shapes
        """
        sum = 0
        for obj in self.my_objects:
            sum += obj.get_per()
        return sum

    def get_colors(self):
        """
        :return: a dictionary with the amount of shapes with each color
        """
        sum_red = 0
        sum_green = 0
        sum_blue = 0
        for obj in self.my_objects:
            if obj.get_color() == "red":
                sum_red += 1
            if obj.get_color() == "green":
                sum_green += 1
            if obj.get_color() == "blue":
                sum_blue += 1
        color_dictionary = {"red": sum_red, "green": sum_green, "blue": sum_blue}
        return color_dictionary


def main():
    """
    run the program
    """
    my_container = MyContainer()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_peremiters())
    print("colors:", my_container.get_colors())


if __name__ == '__main__':
    main()
