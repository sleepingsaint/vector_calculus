# Scalar Field

## Definition

A scalar field associates a scalar value to every point in a space – possibly physical space. The scalar may either be a mathematical number or a physical quantity. 

> This library provides __ScalarField__ class to handle the implementation and processing of scalar fields

There are two ways you can define Scalar Field
* If you have data itself
* Have a function with gives output value based on the location in the space

## Usage

```python
import vector_calculus as vec

# use this method when you have data points
sf1 = vec.ScalarField(field, origin, dist)

# use this method when you have the space
# and want to generate the field based on location in space
sf2 = vec.ScalarField.loadField(origin, fun, x, y, z, dist)
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

define a scalar field sf1 using one of the above initializing methods 

### Visualisation

```python
# visualising the scalar field
sf1.show()
```
!> show method takes two optional parameters

#### title (_optional_)
title for the plot
* __data type__ string
* __default__ Scalar Field

#### x, y, z(_optional_)
denoting the extent of the coordinate axes
* __data type__ tuple of size two indicating the starting and ending points
* __default__ (0, lenght of the axis - 1)

### Gradient

```python
# Gradient of the scalar field
vgrad = sf1.grad()
```

## Example

Given scalar field sf = x3yx
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
    val = pow(loc[0], 3) * loc[1] * loc[2]
    return val

sf = vec.ScalarField.loadField([0, 0, 0], field, x_space, y_space, z_space)
sf.show(title="Visualising the scalar field sf")

grad = sf.gradient()
grad.show(title="Gradient of scalar field sf")
```

![Figure_1](https://user-images.githubusercontent.com/35530053/99910066-0a46b780-2d12-11eb-9545-12c4275ce035.png)
> Visualises the scalar field sf

![Figure_2](https://user-images.githubusercontent.com/35530053/99910080-1894d380-2d12-11eb-80af-728f73228bcc.png)
> Visualises the gradient of the scalar field sf