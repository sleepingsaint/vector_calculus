import numpy as np
from .vector import Vector
import matplotlib.pyplot as plt

class VectorField:
    # dx, dy, dz defines the spacing between the co-ordinates
    def __init__(self, field, origin=[0, 0, 0], dist=[1, 1, 1]):
        self.field = np.array(field)
        self.origin = origin
        self.dist = dist

    def __repr__(self):
        return "Vector Field {}".format(self.field.shape)

    def __str__(self):
        return "Vector Field {}".format(self.field.shape)

    def __add__(self, val):
        if isinstance(val, VectorField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return VectorField(self.field + val.field)
        return VectorField(self.field + val)

    def __sub__(self, val):
        if isinstance(val, VectorField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return VectorField(self.field - val.field)
        return VectorField(self.field - val)

    def __mul__(self, val):
        if isinstance(val, VectorField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return VectorField(self.field * val.field)
        return VectorField(self.field * val)

    def __pow__(self, val):
        if isinstance(val, VectorField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return VectorField(self.field ** val.field)
        return VectorField(self.field ** val)

    def __truediv__(self, val):
        if isinstance(val, VectorField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return VectorField(self.field / val.field)
        return VectorField(self.field / val)

    def __floordiv__(self, val):
        if isinstance(val, VectorField):
            if(self.field.shape != val.field.shape):
                raise TypeError(
                    "Dimensions of the arguments are different {}, {}".format(self.field.shape, val.field.shape))
            return VectorField(self.field // val.field)
        return VectorField(self.field // val)

    def divergence(self):
        x_comp = []
        y_comp = []
        z_comp = []

        for loc, vec in np.ndenumerate(self.field):
            x_comp.append(vec.x)
            y_comp.append(vec.y)
            z_comp.append(vec.z)

        x_comp = np.array(x_comp).reshape(self.field.shape)
        y_comp = np.array(y_comp).reshape(self.field.shape)
        z_comp = np.array(z_comp).reshape(self.field.shape)

        _dz = np.gradient(x_comp, self.dist[2], axis=0) + np.gradient(z_comp,
                                                                      self.dist[2], axis=0) + np.gradient(y_comp, self.dist[2], axis=0)
        _dx = np.gradient(x_comp, self.dist[0], axis=1) + np.gradient(z_comp, self.dist[0],
                                                                      axis=1) + np.gradient(y_comp, self.dist[0], axis=1)
        _dy = np.gradient(x_comp, self.dist[1], axis=2) + np.gradient(z_comp, self.dist[1],
                                                                      axis=2) + np.gradient(y_comp, self.dist[1], axis=2)

        return (_dx + _dy + _dz)

    def curl(self):
        if(self.field.ndim == 2):
            x_comp = []
            y_comp = []

            for loc, vec in np.ndenumerate(self.field):
                x_comp.append(vec.x)
                y_comp.append(vec.y)

            x_comp = np.array(x_comp).reshape(self.field.shape)
            y_comp = np.array(y_comp).reshape(self.field.shape)

            x_comp_y = np.gradient(x_comp, self.dist[0], axis=1)
            y_comp_x = np.gradient(y_comp, self.dist[2], axis=0)

            curl_z = y_comp_x - x_comp_y

            temp = []

            for loc, curl in np.ndenumerate(curl_z):
                temp.append(Vector(0, 0, curl))

            temp = np.array(temp)
            temp.resize(self.field.shape)

            return VectorField(temp)

        elif self.field.ndim == 3:

            x_comp = []
            y_comp = []
            z_comp = []

            for loc, vec in np.ndenumerate(self.field):
                x_comp.append(vec.x)
                y_comp.append(vec.y)
                z_comp.append(vec.z)

            x_comp = np.array(x_comp).reshape(self.field.shape)
            y_comp = np.array(y_comp).reshape(self.field.shape)
            z_comp = np.array(z_comp).reshape(self.field.shape)

            x_comp_y = np.gradient(x_comp, self.dist[1], axis=2)
            x_comp_z = np.gradient(x_comp, self.dist[2], axis=0)

            y_comp_x = np.gradient(y_comp, self.dist[0], axis=1)
            y_comp_z = np.gradient(y_comp, self.dist[2], axis=0)

            z_comp_x = np.gradient(z_comp, self.dist[0], axis=1)
            z_comp_y = np.gradient(z_comp, self.dist[1], axis=2)

            curl_x = z_comp_y - y_comp_z
            curl_y = x_comp_z - z_comp_x
            curl_z = y_comp_x - x_comp_y

            temp = []

            for loc, curl in np.ndenumerate(curl_x):
                if len(loc) == 1:
                    temp.append(Vector(curl, curl_y[loc[0]], curl_z[loc[0]]))
                elif len(loc) == 2:
                    temp.append(
                        Vector(curl, curl_y[loc[0]][loc[1]], curl_z[loc[0]][loc[1]]))
                elif len(loc) == 3:
                    temp.append(
                        Vector(curl, curl_y[loc[0]][loc[1]][loc[2]], curl_z[loc[0]][loc[1]][loc[2]]))

            temp = np.array(temp)
            temp.resize(self.field.shape)

            return VectorField(temp)

    # scale is used for arrows length

    def show(self, x=(), y=(), z=(), scale=0.2, title="Vector Field"):
        if(self.field.ndim == 1):
            x_axis = []
            c_x = []
            c_y = []
            c_z = []

            if len(x) != 0:
                x_axis = np.linspace(x[0], x[1], self.field.shape[0])

            for loc, vec in np.ndenumerate(self.field):
                if len(x) == 0:
                    x_axis.append(loc[0])
                c_x.append(vec.x)
                c_y.append(vec.y)
                c_z.append(vec.z)

            x_axis = np.array([x*self.dist[0] + self.origin[0]
                               for x in x_axis])
            y_axis = np.array([0 for x in range(0, len(x_axis))])
            z_axis = np.array([0 for x in range(0, len(x_axis))])

            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            ax.quiver(x_axis, y_axis, z_axis, c_x, c_y,
                      c_z, length=1 * scale, normalize=True)

            ax.set_xlabel("x axis")
            ax.set_ylabel("y axis")
            ax.set_zlabel("z axis")
            
            plt.title(title)
            plt.show()
        
        elif(self.field.ndim == 2):
            x_axis = []
            y_axis = []

            c_x = []
            c_y = []
            c_z = []

            if len(x) != 0 and len(y) != 0:
                x_axis, y_axis = np.meshgrid(
                    np.linspace(x[0], x[1], self.field.shape[0]),
                    np.linspace(y[0], y[1], self.field.shape[1])
                )

            for loc, vec in np.ndenumerate(self.field):

                if len(x) == 0 or len(y) == 0:
                    x_axis.append(loc[0])
                    y_axis.append(loc[1])

                c_x.append(vec.x)
                c_y.append(vec.y)
                c_z.append(vec.z)

            x_axis = np.array([x*self.dist[0] + self.origin[0]
                               for x in x_axis])
            y_axis = np.array([y*self.dist[1] + self.origin[1]
                               for y in y_axis])
            z_axis = np.array([0 for x in range(0, x_axis.size)])

            x_axis = np.array(x_axis)
            y_axis = np.array(y_axis)
            z_axis = np.array(z_axis)

            c_x = np.array(c_x).reshape(self.field.shape)
            c_y = np.array(c_y).reshape(self.field.shape)
            c_z = np.array(c_z).reshape(self.field.shape)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            ax.quiver(x_axis, y_axis, z_axis, c_x, c_y,
                      c_z, length=1 * scale, normalize=True)

            ax.set_xlabel("x axis")
            ax.set_ylabel("y axis")
            ax.set_zlabel("z axis")
            
            plt.title(title)
            plt.show()

        elif(self.field.ndim == 3):
            x_axis = []
            y_axis = []
            z_axis = []

            c_x = []
            c_y = []
            c_z = []

            if len(x) != 0 and len(y) != 0 and len(z) != 0:
                z_axis, x_axis, y_axis = np.meshgrid(
                    np.linspace(z[0], z[1], self.field.shape[0]),
                    np.linspace(x[0], x[1], self.field.shape[1]),
                    np.linspace(y[0], y[1], self.field.shape[2])
                )

            for loc, vec in np.ndenumerate(self.field):
                if len(x) == 0 or len(y) == 0:
                    x_axis.append(loc[0])
                    y_axis.append(loc[1])
                    z_axis.append(loc[2])
                c_x.append(vec.x)
                c_y.append(vec.y)
                c_z.append(vec.z)

            x_axis = np.array([x*self.dist[0] + self.origin[0]
                               for x in x_axis])
            y_axis = np.array([y*self.dist[1] + self.origin[1]
                               for y in y_axis])
            z_axis = np.array([z*self.dist[2] + self.origin[2]
                               for z in z_axis])

            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            ax.quiver(x_axis, y_axis, z_axis, c_x, c_y,
                      c_z, length=1 * scale, normalize=True)

            ax.set_xlabel("x axis")
            ax.set_ylabel("y axis")
            ax.set_zlabel("z axis")

            plt.title(title)
            plt.show()

    # here origin defines where all the user axes starts
    # fun takes in the location and gives the resultant
    # vector at that point
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
                field.append(
                    fun((_x, _y, _z)))

        field = np.array(field).reshape(np.array(x).shape)

        if(len(origin) == 2):
            origin.append(0)

        return VectorField(field, origin=origin, dist=dist)
