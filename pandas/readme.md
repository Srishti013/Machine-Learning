## PANDAS

#### Series Declaration

```python

s = pd.series([1,2,3], index =['a','b','c'])   # OR s = pd.Series({'a':1,'b':2,'c':3})
print(s)  

# OUTPUT:
#          a  1
#          b  2
#          c  3

```

#### DataFrame

```python

x = pd.DataFrame([[1,2],[3,4]],columns = ['c1','c2'], index = ['r1','r2'])
print(x)

# OUTPUT:
#          c1   c2
#     r1   1     2
#     r2   3     4

# Drop

x_drop =x.drop(labels = ['c2'])   # This drops column c2 from the dataframe and assigns it to x_drop


# Append

x_append = x.append([5,6], index = ['r3'])   # This appends r3 to the dataframe

```


#### Concatenation and Merging

```python

pd.concat([arr1,arr2], axis =1)     # Concatenates the two dataframes columwise (By default vale of axis is 0)

pd.merger(arr1,arr2)         # This function results a dataframe which has the rows which had the same values for the common columns of both the dataframes

```

