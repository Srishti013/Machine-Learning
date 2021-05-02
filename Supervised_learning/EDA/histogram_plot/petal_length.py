# Import plotting modules
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

#loading dataset
iris=datasets.load_iris()
sns.set()

#plotting histogram
_=plt.hist(versicolor_petal_length)
plt.show()

