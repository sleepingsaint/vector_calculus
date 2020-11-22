# Vector Field

## Definition

In vector calculus and physics, a vector field is an assignment of a vector to each point in a subset of space. For instance, a vector field in the plane can be visualised as a collection of arrows with a given magnitude and direction, each attached to a point in the plane.

> This library provides __VectorField__ class to handle the implementation and processing of vector field.

VectorField can be implemented in two ways:
* If you have data itself
* Have a function with gives output value based on the location in the space

## Usage

```python
import vector_calculus as vec

# use this method when you have data points
vf1 = vec.VectorField(field, origin, dist)        

# use this method when you have the space
# and want to generate the field based on location in space
vf2 = vec.VectorField.loadField(origin, fun, x, y, z, dist)
```

## Parameters

### field (_required_)
denotes the scalar field
* __data type__ n-dimensional numpy array

### origin (_optional_)
denotes the starting point of the field
* __data type__ list of length 3 indicating the x, y, z coordinates of your space.
* __default__ value [0, 0, 0]

### dist (_optional_)
denotes the spacing between the x, y, z coordinates of your space.
* __data type__ list of length 3 indicating the x, y, z separation distance
* __default__ value [1, 1, 1]

### fun (_required_)
it return the field value by taking the x, y, z values of the location
* __data type__ python function

### x, y (_required_), z (_optional_)
denotes the axes of your space
* __data type__ list or numpy array

## Operations

define a vector field vf1 using one of the above initializing methods

### Visualisation

```python
# visualising the vector field
vf1.show()
```
!> show method takes two optional parameters

#### title (_optional_)
title for the plot
* __data type__ string
* __default__ Vector Field

#### x, y, z(_optional_)
denoting the extent of the coordinate axes
* __data type__ tuple of size two indicating the starting and ending points
* __default__ (0, lenght of the axis - 1)

### Divergence

In vector calculus, divergence is a vector operator that operates on a vector field, producing a scalar field giving the quantity of the vector field's source at each point.

```python
# divergence of the vector field
vdiv = vf1.divergence()
```

### Curl

The curl of a field is formally defined as the circulation density at each point of the field. A vector field whose curl is zero is called irrotational. The curl is a form of differentiation for vector fields.

```python
# curl of the vector field
vcurl = vf1.curl
```

### Example

Vector field vf = x3yz i - x4y k

```python
import numpy as np
import vector_calculus as vec

x_extent, y_extent, z_extent = 0.1, 0.1, 0.1
pts_x, pts_y, pts_z = 5, 5, 5
x = np.linspace(-1*x_extent, x_extent, pts_x)
y = np.linspace(-1*y_extent, y_extent, pts_y)
z = np.linspace(-1*z_extent, z_extent, pts_z)

x_space, y_space, z_space = np.meshgrid(x, y, z)
def field(loc):
    x_comp = pow(loc[0], 3) * loc[1] * loc[2]
    y_comp = 0
    Z_comp = pow(loc[0], 4) * loc[1]
    return vec.Vector(x_comp, y_comp, z_comp)

vf = vec.VectorField.loadField([0, 0, 0], field, x_space, y_space, z_space)
vf.show(title="Vector Field vf")

curl =vf.curl()
curl.show(title="Curl of vector field vf")
```


![Figure_1](https://user-images.githubusercontent.com/35530053/99910681-5f37fd00-2d15-11eb-8a27-5d0225b1b392.png)

> Visualisation of the vector field vf

![Figure_2](https://user-images.githubusercontent.com/35530053/99910706-8262ac80-2d15-11eb-83db-85cf04720449.png)

> Visualisation of the curl of the vector field vf
