"""
Name: <Juyeoung Kim>
<sphere>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""

import math


class Sphere:
    """
    represents radius, area of sphere, volume of sphere
    """
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        surface_area = (4 * math.pi * (self.radius ** 2))
        return float(surface_area)

    def volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return float(volume)
