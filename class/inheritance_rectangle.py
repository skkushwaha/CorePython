class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return self.width * 2 + self.height * 2
class Cuboid(Rectangle):
    def __init__(self, width, height, length):
        self.length = length
        super().__init__(width, height)

    def volume(self):
        return self.length * self.width * self.height

c = Cuboid(100, 200, 150)
print(c.area())
print(c.perimeter())
print(c.volume())
