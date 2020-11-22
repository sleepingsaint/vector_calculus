# Vector

## Definition

A vector is an object that has both a magnitude and a direction. Geometrically, we can picture a vector as a directed line segment, whose length is the magnitude of the vector and with an arrow indicating the direction. The direction of the vector is from its tail to its head.

In the Electromagnetics domain most of the problems we encounter are related to vectors. So having a easy and efficient implementation of vector is really important.

> This library provides Vector class to handle the operations on vectors.

## Usage

```python
import vector_calculus as vec

# two dimensional vector
v1 = vec.Vector(1, 2)     

# three dimensional vector
v2 = vec.Vector(1, 1, 1)    
```

## Vector Operations

### Dot product

> __*__ operator can be used for dot product

```python
import vector_calculus as vec

v1 = vec.Vector(1, 1, 1)
v2 = vec.Vector(1, 2, 2)
k = 3 

# these three variables v1, v2, k will be used to demonstrate 
# the remaining examples on this page

# dot product
vdot = v1 * v2
```

### Cross Product

> __**__ operator can be used for dot product


```python
# cross product
vcross = v1 ** v2
```

## Basic Operations

### Addition
```python
# vector addition
vadd = v1 + v2
vaddk = v1 + k 
```

### Subtraction
```python
# vector subtraction
vsub = v1 - v2
vsubk = v1 - k 
```

### Multiplication
```python
# vector multiplication
vmul = v1 * k # Vector(3, 3, 3)
```

### Division
```python
# vector division
vdiv = v1 / k # Vector(0.33, 0.33, 0.33)
```

### Power
```python
vpow = v2 ** k # Vector(1, 8, 8)
```

!> In multiplication, division and power functions the constant should be second operator.

### Magnitude
```python
# vector magnitude
vmag = v1.mag() # 1.732
```

### Equality
```python
print(v1 == v2) # False
print(v1 == v1) # True
```