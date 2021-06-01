## Data Manipulation with pandas

#### Most used methods and attributes:<br>
    - .info()
    - .describe()
    - .shape
    - .columns
    - .index()
    
     
#### Sorting
    - .sort_values(ascending=True) (if you want descending then set ascending to False) 
   
#### Selecting rows
    - dataset["col"]>100 ----> (will select rows where value of col>100, and print only one column with true and false in it)
    - dataset[dataset["col"]>100] -------> will print all columns and rows meetin req. condition
    
#### Filtering using categorical variables
    -  lst = ["s1", "s2", "s3"]<br>
      condn = dataset["col"].isin(lst)<br>
      dataset[condn]  --->  will only print rows where col= s1,s2 or s3
      
#### Feature Engineering
    - Involves adding new columns to the data using previous columns
    - Ex: dataset["new_col"] = dataset["old_col"] * 2 
   
#### Summary Statistics
    - .mean(), .median(), .sum()
    - .min(), .max(), .std(), .var()
    - .quantile(number(0 to 1))
    - dataset['column'].agg(summary_stat) -----> gives summary stat(mean, median, min etc) of the whole column
    - cumsum(), cumprod(), cummax(), cummin() -----> return a whole column
#### Counting
    -  .drop_duplicates(subset="col_name")
    -  .value_counts(sort=True/False, normalize=True/False)
#### Gropued Summary Statistics
    - .groupby("attribute")["col_name"].mean() ---> for grouped mean
    - .groupby("attribute")["col_name"].agg([min, max,sum]) ---> for grouped min max and sum
#### Pivot Tables
    - .pivot_table(values="col_name", index="attribute1", columns="attribute2", aggfunc=np.mean,fill_value = 0, margins=True/False)
### Explict Indexing
    - .set_index("col_name") --->multiple columns can also be set as indices
    - .reset_index(drop=True/False)
    - .isin()
    - .loc[]
    - .sort_index(level=[],ascending=[])
    - .iloc[]
#### Visualising Data
    - .hist(bins=any_number, alpha= number_btw_0_and_1)
    - .plot(kind="bar", title="")  ----> best for categorical vs numeric
    - .plot(kind="line", x="", y="", title="", rot=number(generally 45)) ----> best for numeric vs numeric
    - .plot(kind="scatter", x="", y="")
    - plt.legend([])
#### Missing Values
    - .isna() ---> returns 2d boolean array
    - .isna().any() ---> returns bool value for each column, telling whether it has missing value or not
    - .isna().sum() ---> sum of missing values in each column
    - .dropna() ---> drops rows with misssing values
    - .fillna(0) ---> replaces missing values with 0

#### Creating Dataframes
    - pd.DataFrame(list_of_dictionaries)
    - pd.DataFrame(dictionary_of_lists)
### Reading and Writing in CSV's
    - .read_csv("filename")
    - updated_file.to_csv("name_of_updated_file.csv")
### Merging tables/Datasets
    * Inner Join
    - dataset1.merge(dataset2,on="common_colname",suffixes=('_x','_y'))
    - dataset1.merge(dataset2, on=['col1','col2','col3']) \
				.merge(dataset3, on='col4')
    * Left Join
    - dataset1.merge(dataset2,on="common_colname",suffixes=('_x','_y'),how="left")
    
    * Right Join
    - dataset1.merge(dataset2,on="common_colname",suffixes=('_x','_y'),how="right")
    
    * Outer Join
    - dataset1.merge(dataset2,on="common_colname",suffixes=('_x','_y'),how="outer")
    
    * Using the above techniques tables can also be merged to themselves if there is 
      some sequel, heirarchical or graph data
    * Whenever using left index or right index as merging columns we have to set 
      left_index=true or right_index= True respectively
