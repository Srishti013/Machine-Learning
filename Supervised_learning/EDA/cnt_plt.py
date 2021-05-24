plt.figure()
sns.countplot(x='feature_name',hue='target_variable',data=dataset,palette='RdBu')
xticks([0,1],['No','Yes']) #when the values are in 0 and 1
plt.show()
