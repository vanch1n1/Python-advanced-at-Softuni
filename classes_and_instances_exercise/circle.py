class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = self.radius * Circle.pi
        return f"{area:.2f}"

    def get_circumference(self):
        circumference = 2*Circle.pi*self.radius
        return f"{circumference:.2f}"


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())





