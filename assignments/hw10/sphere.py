import math


class Sphere:

    def __init__(self, radius):
        self.radius = radius
        self.surface_area = (4 * math.pi * (radius ** 2))
        self.volume = (4 / 3) * math.pi * (radius ** 3)

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return self.surface_area()

    def volume(self):
        return self.volume

