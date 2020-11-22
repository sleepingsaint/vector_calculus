import numpy as np


class Vector:

    def __init__(self, x, y, z=0):
        self.coordinates = np.array([x, y, z])
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector [{}, {}, {}]".format(self.x, self.y, self.z)

    def __repr__(self):
        return "Vector [{}, {}, {}]".format(self.x, self.y, self.z)

    def __add__(self, vec):
        if(isinstance(vec, Vector)):
            return Vector(*(self.coordinates + vec.coordinates))
        return Vector(*(self.coordinates + vec))

    def __sub__(self, vec):
        if(isinstance(vec, Vector)):
            return Vector(*(self.coordinates - vec.coordinates))
        return Vector(*(self.coordinates - vec))

    def __mul__(self, vec):
        if(isinstance(vec, Vector)):
            return np.dot(self.coordinates, vec.coordinates)
        return Vector(*(self.coordinates * vec))

    def __pow__(self, vec):
        if(isinstance(vec, Vector)):
            return Vector(*(np.cross(self.coordinates, vec.coordinates)))
        return Vector(*(self.coordinates ** vec))

    def __truediv__(self, val):
        return Vector(*(self.coordinates / val))

    def __floordiv__(self, val):
        return Vector(*(self.coordinates // val))

    def __eq__(self, vec):
        return (self.x == vec.x) and (self.y == vec.y) and (self.z == vec.z)

    def __ne__(self, vec):
        return (self.x != vec.x) or (self.y != vec.y) or (self.z != vec.z)

    def __iter__(self):
        for x in self.coordinates:
            yield x

    def __getitem__(self, item):
        print("iam called, {}".format(item))
        return self.coordinates[item]

    def mag(self):
        return np.linalg.norm([self.x, self.y, self.z])