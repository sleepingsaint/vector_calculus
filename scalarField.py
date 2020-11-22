import numpy as np
import matplotlib.pyplot as plt
from .vector import Vector
from .vectorField import VectorField as vf


class ScalarField:

    def __init__(self, field, origin=[0, 0, 0], dist=[1, 1, 1]):
        self.field = np.array(field)
        self.origin = origin
        self.dist = dist

    def __str__(self):
        return "ScalarField {}".format(self.field.shape)

    def __repr__(self):
        return "ScalarField {}".format(self.field.shape)

    def __add__(self, val):
        if isinstance(val, ScalarField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return ScalarField(self.field + val.field)
        return ScalarField(self.field + val)

    def __sub__(self, val):
        if isinstance(val, ScalarField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return ScalarField(self.field - val.field)
        return ScalarField(self.field - val)

    def __mul__(self, val):
        if isinstance(val, ScalarField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return ScalarField(self.field * val.field)
        return ScalarField(self.field * val)

    def __pow__(self, val):
        if isinstance(val, ScalarField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return ScalarField(self.field ** val.field)
        return ScalarField(self.field ** val)

    def __truediv__(self, val):
        if isinstance(val, ScalarField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return ScalarField(self.field / val.field)
        return ScalarField(self.field / val)

    def __floordiv__(self, val):
        if isinstance(val, ScalarField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return ScalarField(self.field // val.field)
        return ScalarField(self.field // val)

    def gradient(self):
        if(self.field.ndim == 2):
            x = np.gradient(self.field, axis=0)
            y = np.gradient(self.field, axis=1)

            result = []

            for loc, val in np.ndenumerate(x):
                result.append(Vector(val, y[loc[0]][loc[1]]))

            result = np.array(result)
            result.resize(self.field.shape)

            return vf(result)

        elif(self.field.ndim == 3):
            z = np.gradient(self.field, self.dist[2], axis=0)
            x = np.gradient(self.field, self.dist[0], axis=1)
            y = np.gradient(self.field, self.dist[1], axis=2)

            result = []
            for loc, val in np.ndenumerate(x):
                result.append(
                    Vector(val, y[loc[0]][loc[1]][loc[2]], z[loc[0]][loc[1]][loc[2]]))

            result = np.array(result)
            result.resize(self.field.shape)

            return vf(result)

    def show(self, x=(), y=(), z=(), title="Scalar Field"):
        fig = plt.figure()
        ranges = self.field.shape

        # 2d field
        if self.field.ndim == 2:
            ax = fig.add_subplot(111)

            x_axis = []
            y_axis = []
            c = []

            for loc, val in np.ndenumerate(self.field):
                if len(x) == 0 or len(y) == 0:
                    x_axis.append(loc[0])
                    y_axis.append(loc[1])
                c.append(val)

            if len(x) != 0 and len(y) != 0:
                x_axis, y_axis = np.meshgrid(np.linspace(
                    x[0], x[1], ranges[0]), np.linspace(y[0], y[1], ranges[1]))

            x_axis = np.array([x*self.dist[0] + self.origin[0]
                               for x in x_axis])
            y_axis = np.array([y*self.dist[1] + self.origin[1]
                               for y in y_axis])

            scatter = ax.scatter(x_axis, y_axis, c=c)

            # adding labels
            plt.xlabel("x axis")
            plt.ylabel("y axis")

            # adding legend
            plt.colorbar(scatter)
            plt.title(title)
            plt.show()

        # 3d field
        if(self.field.ndim == 3):
            ax = fig.add_subplot(111, projection="3d")

            x_axis = []
            y_axis = []
            z_axis = []
            c = []

            for loc, val in np.ndenumerate(self.field):
                if len(x) == 0 or len(y) == 0 or len(z) == 0:
                    z_axis.append(loc[0])
                    x_axis.append(loc[1])
                    y_axis.append(loc[2])
                    c.append(val)

            if len(x) != 0 and len(y) != 0 and len(z) != 0:
                x_axis, y_axis, z_axis = np.meshgrid(
                    np.linspace(z[0], z[1], ranges[0]),
                    np.linspace(x[0], x[1], ranges[1]),
                    np.linspace(y[0], y[1], ranges[2])
                )

            x_axis = np.array([x*self.dist[0] + self.origin[0]
                               for x in x_axis])
            y_axis = np.array([y*self.dist[1] + self.origin[1]
                               for y in y_axis])
            z_axis = np.array([z*self.dist[2] + self.origin[2]
                               for z in z_axis])

            scatter = ax.scatter(x_axis, y_axis, z_axis, c=c)

            # adding labels
            ax.set_xlabel("x axis")
            ax.set_ylabel("y axis")
            ax.set_zlabel("z axis")

            # adding legend
            plt.colorbar(scatter)
            plt.title(title)
            plt.show()

    # here origin defines where all the user axes starts
    # fun takes in the location and gives the resultant
    # value / scalar at that location
    # x, y, z represents the axes generated using meshgrid
    @classmethod
    def loadField(cls, origin, fun, x, y, z=[], dist=[1, 1, 1]):
        field = []

        if len(z) == 0:
            for loc, _x in np.ndenumerate(np.array(x)):
                _y = y[loc[0]][loc[1]]
                field.append(fun((_x, _y)))
        else:
            for loc, _x in np.ndenumerate(np.array(x)):
                _y = y[loc[0]][loc[1]][loc[2]]
                _z = y[loc[0]][loc[1]][loc[2]]
                field.append(fun((_x, _y, _z)))

        field = np.array(field).reshape(np.array(x).shape)

        if(len(origin) == 2):
            origin.append(0)

        return ScalarField(field, origin=origin, dist=dist)
