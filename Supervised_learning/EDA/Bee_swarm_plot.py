#creating plot
_=sns.swarmplot(x='species',y='petal length (cm)',data=df)

# Labeling axes
_=plt.xlabel('species')
_=plt.ylabel('petal length (cm)')

# Showing the plot
plt.show()
