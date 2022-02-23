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

print( np.random.randint(3,high=6,size=2)) # --> Prints array with numbers in the range [3,6) of size 2

# np.random.seed() --> is used to get same typr of random numbers when the seed is same

# np.random.shuffle()
arr = np.array([1,2,3,4])
print(np.random.shuffle(arr)) --> shuffles the array element, example output: [2,3,4,1]

# np.random.normal(loc=x,scale=y)
# here loc and scale represent mean and standard deviation of a normal distribution

# np.random.uniform()
# Used to get numbers from uniform distribution

```


#### Indexing

```python

arr = np.array([1,2,3,4])

print(arr[0])   # prints the first element --> 1
print(arr[:2])  # prints all elements from starting till at 2 --> [1,2]
print(arr[-2:])  # prints all elements from index -2 till end --> [3,4]


arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])
print(np.argmin(arr[0]))    # Prints index of the minimum element in the first row --> 2
print(np.argmax(arr[2]))    # Prints index of the maximum element in the third row --> 1
print(np.argmin(arr,axis=0))  # Prints array of indices of minimum elements in each column  --> [2,0,1]
print(np.argmin(arr,axis=1))  # Prints array of indices of minimum elements in each row  --> [2,2,0]

```

#### Filtering

```python

arr = np.array([0, 3, 5, 3, 1])
print(np.where(arr == 3))  # Prints array of indices where given condition is true --> [1,3]

# np.where() has three arguments : 1) main array or condition , 2) values to replace true values, 3) values to replace false values

positives = np.array([[1, 2], [3, 4]])
negatives = np.array([[-2, -5], [-1, -8]])
np_filter = positives > 2
print(np.where(np_filter, positives, negatives)) # [[-2,-5],[3,4]]

# np.any() works like the OR operation and np.all() works like the and operation

arr = np.array([1,2,3,0])
print(np.any(arr==0)) # True
print(np.all(arr==0)) # False

```

#### Statistical Functions

```python

arr.min() # Prints minimum element in arr
arr.max() # Prints maximum element in arr
np.mean(arr)  # Prints mean of elements in arr
np.median(arr)  # Prints median of elements in arr
np.var(arr)  # Prints variance of elements in arr
np.sum(arr)  # prints sum of elements of arr
np.cumsum(arr)  # prints array of cummalative sum of elements of arr
np.concatenate([arr1,arr2])  # Concatenates arr1 and arr2

```
