## Numpy

#### Array declaration
```python

# declaring a numpy array of type float
arr = np.array([[0, 1, 3], [0, 4, 5]],
               dtype=np.float32)
               
```

#### Copy

By default refernce to a numpy array does not create a copy of the array. So, if we make a change to the reference then the change is also reflected to the original
array. That is why using a .copy() helps, as it creates a copy of the original numpy array.

```python

a = np.array([0, 1])
b = np.array([9, 8])
c = a
print('Array a: {}'.format(repr(a))) # Array a: array([0, 1])
c[0] = 5
print('Array a: {}'.format(repr(a))) # Array a: array([5, 1])

d = b.copy()
d[0] = 6
print('Array b: {}'.format(repr(b))) # Array b: array([9, 8])
print('Array d: {}'.format(repr(d))) # Array d: array([6, 8])

```

#### Casting 

```python

# Helps in changing the type of numpy array
arr = np.array([1, 2])
print(arr.dtype) # int64
arr = arr.astype(np.float32) 
print(arr.dtype) # float32

```

#### NAN and Infinity

* np.nan is as a filler value for incomplete data.
* np.nan cannot take on an integer type.
* To represent infinity in NumPy, we use the np.inf.
* We can also represent negative infinity with -np.inf.
* np.inf cannot take on an integer type.

#### .arange() and .linspace()


```python

arr = np.arange(-1, 4)
print(arr) # [-1  0  1  2  3]

arr = np.linspace(5, 11, num=4, endpoint=False)
print(arr) # [5. , 6.5, 8. , 9.5]

```


#### Reshaping 

```python

arr = np.arange(8)

reshaped_arr = np.reshape(arr, (2, 4))
print(reshaped_arr)
# [[0,1,2,3]
#   [4,5,6,7]]
   
# To transform an array to a 1-D array use .flatten()

print(arr.flatten())
# [0,1,2,3,4,5,6,7]

# To get a transpose
arr = np.reshape(arr,(2,4))
arr = np.transpose(arr)
print(arr.shape()) # (4,2)

   
````


#### Zeroes and Ones

```python

arr = np.zeroes(4)
arr1 = np.ones(2)
print(arr) # [0,0,0,0]
print(arr1) # [1,1]

arr = np.array([[1,2],[3,4]])
arr0 = np.zeros_like(arr)
print(arr0) 
# [[0,0]
#  [0,0]]
arr1 = np.ones_like(arr)
print(arr1)
# [[1,1]
#  [1,1]]

```


#### Arithmetic Operations

```python

arr = np.array([[1, 2], [3, 4]])
# Add 1 to element values
print(repr(arr + 1))
# Subtract element values by 1.2
print(repr(arr - 1.2))
# Double element values
print(repr(arr * 2))
# Halve element values
print(repr(arr / 2))
# Integer division (half)
print(repr(arr // 2))
# Square element values
print(repr(arr**2))
# Square root element values
print(repr(arr**0.5))

```

#### Numpy random module

```python

print( np.random.randint(3,high=6)) # --> Prints a random number in the range [3,6)
