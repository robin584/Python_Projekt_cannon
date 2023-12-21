'''class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        """Overloaded subtraction operator."""
        return vector(self.x - other.x, self.y - other.y)

    def __abs__(self):
        """Return the magnitude of the vector."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def move(self, speed):
        """Move the vector by the given speed."""
        self.x += speed.x
        self.y += speed.y
'''


class vector:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color

    def __sub__(self, other):
        """Overloaded subtraction operator."""
        return vector(self.x - other.x, self.y - other.y)

    def __abs__(self):
        """Return the magnitude of the vector."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def move(self, speed):
        """Move the vector by the given speed."""
        self.x += speed.x
        self.y += speed.y
