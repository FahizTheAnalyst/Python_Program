
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def compare_area(self, other):
        if self.area() > other.area():
            return "First rectangle is larger."
        elif self.area() < other.area():
            return "Second rectangle is larger."
        return "Both rectangles are equal in area."


length1 = float(input("Enter the length of the first rectangle: "))
breadth1 = float(input("Enter the breadth of the first rectangle: "))
rect1 = Rectangle(length1, breadth1)


length2 = float(input("Enter the length of the second rectangle: "))
breadth2 = float(input("Enter the breadth of the second rectangle: "))
rect2 = Rectangle(length2, breadth2)


print(f"Area of first rectangle: {rect1.area()}, Perimeter: {rect1.perimeter()}")
print(f"Area of second rectangle: {rect2.area()}, Perimeter: {rect2.perimeter()}")
print(rect1.compare_area(rect2))
