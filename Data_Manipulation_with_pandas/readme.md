### Data Manipulation with pandas

* Three most used methods and attributes:<br>
    - .info()
    - .describe()
    - .shape
     
* Sorting
   - .sort_values(ascending=True) (if you want descending then set ascending to False) 
   
* Selecting rows
    - dataset["col"]>100 ----> (will select rows where value of col>100, and print only one column with true and false in it)
    - dataset[dataset["col"]>100] -------> will print all columns and rows meetin req. condition
    
* Filtering using categorical variables
   -  lst = ["s1", "s2", "s3"]<br>
      condn = dataset["col"].isin(lst)<br>
      dataset[condn]  --->  will only print rows where col= s1,s2 or s3
      
* Feature Engineering
   - Involves adding new columns to the data using previous columns
   - Ex: dataset["new_col"] = dataset["old_col"] * 2 
