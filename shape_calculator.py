class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        return

    def set_height(self, height):
        self.height = height
        return

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        s = ""
        i = 0
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        while i != self.height:
            s += "*" * self.width
            s += "\n"
            i += 1
        return s

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, side=0):
        self.side = self.width = self.height = side

    def __repr__(self):
        return f"Square(side={self.side})"

    def set_width(self, side):
        self.side = side
        return f"Square(side={side})"

    def set_side(self, side):
        self.side = side
        return f"Square(side={side})"

    def get_picture(self):
        s = ""
        i = 0
        while i != self.side:
            s += "*" * self.side
            s += "\n"
            i += 1
        return s
