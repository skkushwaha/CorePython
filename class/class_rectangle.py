class Rectangle:
    count = 0
    def __init__(self, l, h):
        self.width = l
        self.height = h
        Rectangle.count += 1
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    @classmethod
    def get_count(cls):
        return cls.count


r1 = Rectangle(5, 5)
r2 = Rectangle(12, 6)
print(r1.area())
print(r1.perimeter())
print(r1.get_count())
print(Rectangle.get_count())