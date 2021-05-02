# Import numpy
import numpy as np

# Compute number of data points: n_data
x=len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
y=np.sqrt(x)

# Convert number of bins to integer: n_bins
y=int(y)


# Plot the histogram
_=plt.hist(versicolor_petal_length,bins=y)

# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()

