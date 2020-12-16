A compilation of all my canonical posts and answers to old questions on Stack Overflow. Topic arrangement mirrors the [User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/). 

If you find any bugs, or need clarification, or see something that can be improved, please feel free to leave a comment under the answer and I'll typically respond within a day. 

If you found any of my content here helpful and wish to thank me, you can upvote my answer! (please don't serial upvote :-) If you'd like to do more, and have more than 75 reputation on Stack Overflow, please consider awarding me with a [bounty](https://stackoverflow.com/help/privileges/set-bounties). 

## Pandas Gotchas 

- Don't iterate over a DataFrame!
	- [How to iterate over rows in a DataFrame in Pandas?](https://stackoverflow.com/a/55557758) 

- Never grow a DataFrame!
	- [Creating an empty Pandas DataFrame, then filling it?](https://stackoverflow.com/a/56746204/4909087)
	- [Add one row to pandas DataFrame](https://stackoverflow.com/a/62734983/4909087)   

- Good habits to build to avoid that dreaded `SettingWithCopyWarning`
	- [How to deal with SettingWithCopyWarning in Pandas?](https://stackoverflow.com/a/53954986) 

- Don't use `inplace=True`!
	- [Understanding inplace=True](https://stackoverflow.com/a/59242208/4909087) 
	- [Pandas - is inplace = True considered harmful or not?](https://stackoverflow.com/q/45570984/4909087) 


## IO tools (text, CSV, HDF5, …)
- [Writing a pandas DataFrame to CSV file](https://stackoverflow.com/a/56241457/4909087)   
- [Import CSV file as a pandas DataFrame](https://stackoverflow.com/a/56231664/4909087)  


## Indexing and selecting data
- [How to implement 'in' and 'not in' for Pandas dataframe](https://stackoverflow.com/a/55554709)   
- [Combine duplicated columns within a DataFrame](https://stackoverflow.com/a/54300430)      
- [Deleting all columns except a few](https://stackoverflow.com/a/54315757)  


## MultiIndex / advanced indexing
- [How do I slice or filter MultiIndex DataFrame levels?](https://stackoverflow.com/questions/53927460/select-rows-in-pandas-multiindex-dataframe)  
- [Selecting columns from pandas MultiIndex](https://stackoverflow.com/a/54337009)
- [Setting DataFrame column headers to a MultiIndex](https://stackoverflow.com/a/54335583)     
- [Reorder levels of MultiIndex in a pandas DataFrame](https://stackoverflow.com/a/62746392/4909087)


## Merge, join, and concatenate
- **Pandas Merging 101**
	- [Merging basics - basic types of joins](https://stackoverflow.com/a/53645883/4909087) (read this first)

	- [Index-based joins](https://stackoverflow.com/a/65167356/4909087)

	- [Generalizing to multiple DataFrames](https://stackoverflow.com/a/65167327/4909087)


	- [Performant Cross join](https://stackoverflow.com/a/53699013/4909087)
	  
- [Cartesian Product in pandas](https://stackoverflow.com/a/65017552/4909087)

## Reshaping and pivot tables
- [Split (explode) pandas dataframe string entry to separate rows](https://stackoverflow.com/a/57122617/4909087)
- [Pandas column of lists, create a row for each list element](https://stackoverflow.com/a/57122831/4909087)  


## Working with text data
- [Convert Columns to String in Pandas](https://stackoverflow.com/a/62978895/4909087)    Introduce `"string"` dtype for pandas >= 1.0.
- [Fast punctuation removal with pandas](https://stackoverflow.com/questions/50444346/fast-punctuation-removal-with-pandas)
- [How to lowercase a pandas dataframe string column if it has missing values?](https://stackoverflow.com/a/56084317/4909087)    

- [String concatenation of two pandas columns](https://stackoverflow.com/a/54298586)
- [Remove unwanted parts from strings in a column](https://stackoverflow.com/a/54302517)  
- [Select by partial string from a pandas DataFrame](https://stackoverflow.com/a/55335207)  
- [Get first letter of a string from column](https://stackoverflow.com/a/55532764)


## Working with missing data
- [How to drop rows of Pandas DataFrame whose value in a certain column is NaN?](https://stackoverflow.com/a/62444845/4909087)  
- [GroupBy columns with NaN (missing) values](https://stackoverflow.com/a/61922965/4909087) 
- [How to check if any value is NaN in a Pandas DataFrame](https://stackoverflow.com/a/53862445/4909087)  
- [Convert pandas.Series from dtype object to float, and errors to nans](https://stackoverflow.com/a/47942854)  
- [How to replace values with None in Pandas data frame in Python?](https://stackoverflow.com/a/55469393) 
- [Locate first and last non NaN values in a Pandas DataFrame](https://stackoverflow.com/a/56748194/4909087) - a discussion on `first_valid_index` and `last_valid_index`

## Categorical data


## Nullable integer data type
- [Pandas: ValueError: cannot convert float NaN to integer](https://stackoverflow.com/a/55704512/4909087)

## Nullable Boolean Data Type
- [Preserve NaN values in pandas boolean comparisons](https://stackoverflow.com/a/60203554/4909087)


## Visualization
- [Compare two DataFrames and output their differences side-by-side](https://stackoverflow.com/a/62687227/4909087)  
- [Pretty Printing a pandas dataframe](https://stackoverflow.com/a/60202636/4909087)


## Computational tools
 

## Group By: split-apply-combine
- [Multiple aggregations of the same column using pandas GroupBy.agg()](https://stackoverflow.com/a/54300159)  
- [Pandas GroupBy.apply method duplicates first group](https://stackoverflow.com/a/56215416/4909087)   
- [Get statistics for each group (such as count, mean, etc) using pandas GroupBy?](https://stackoverflow.com/a/55564299)  
- [GroupBy pandas DataFrame and select most common value](https://stackoverflow.com/a/54304691)    
- [Python Pandas Create New Column with Groupby().Sum()](https://stackoverflow.com/a/54417351)   
- [How to get number of groups in a groupby object in pandas?](https://stackoverflow.com/a/46512052)    


## Time series / date functionality
- [pandas datetime to unix timestamp seconds](https://stackoverflow.com/a/54313505/4909087)

## Time deltas


## Styling


## Options and settings


## Performance 
- [For loops with pandas - When should I care?](https://stackoverflow.com/questions/54028199/for-loops-with-pandas-when-should-i-care) 
- [Dynamic Expression Evaluation in pandas using pd.eval()](https://stackoverflow.com/questions/53779986/dynamic-expression-evaluation-in-pandas-using-pd-eval) 
- [When should I (not) want to use pandas apply() in my code?](https://stackoverflow.com/questions/54432583/when-should-i-ever-want-to-use-pandas-apply-in-my-code)  
- [Performant cartesian product (CROSS JOIN) with pandas](https://stackoverflow.com/questions/53699012/performant-cartesian-product-cross-join-with-pandas)  
- [What is the performance impact of non-unique indexes in pandas?](https://stackoverflow.com/a/54317984)  


## Scaling to large datasets


## Sparse data structures

## Frequently Asked Questions (FAQ)
- [How to iterate over rows in a DataFrame in Pandas?](https://stackoverflow.com/a/55557758)   
- [What is the difference between Series.replace and Series.str.replace?](https://stackoverflow.com/questions/56625031/what-is-the-difference-between-series-replace-and-series-str-replace)  
- [Add column of empty lists to DataFrame](https://stackoverflow.com/a/62141252/4909087)  
- [Change data type of columns in Pandas](https://stackoverflow.com/a/60278450/4909087)  
- [Drop rows containing empty cells from a pandas DataFrame](https://stackoverflow.com/a/56708633/4909087)  
- [How to get rid of “Unnamed: 0” column in a pandas DataFrame?](https://stackoverflow.com/a/54358758/4909087)  
- [Difference between map, applymap and apply methods in Pandas](https://stackoverflow.com/a/56300992/4909087)  
- [Convert list of dictionaries to a pandas DataFrame](https://stackoverflow.com/a/53831756)    
- [Find the max of two or more columns with pandas](https://stackoverflow.com/a/54299629) 
- [Sorting by absolute value without changing the data](https://stackoverflow.com/a/54299995)  
- [How do I convert a pandas column or index to a Numpy array?](https://stackoverflow.com/a/54324513)  
- [Convert pandas dataframe to NumPy array](https://stackoverflow.com/a/54508052)
- [Logical operators for boolean indexing in Pandas](https://stackoverflow.com/a/54358361) 
- [What is the difference between size and count in pandas?](https://stackoverflow.com/a/54364400)    
- ['DataFrame' object has no attribute 'sort'](https://stackoverflow.com/a/54399214)
- [Python pandas insert list into a cell](https://stackoverflow.com/a/54399996)
- [How to add a suffix (or prefix) to each column name?](https://stackoverflow.com/a/54410631)  
- [How do I get the row count of a Pandas dataframe?](https://stackoverflow.com/a/55435185)   
- [Rename a specific column in pandas](https://stackoverflow.com/a/46146667)  
- [Get list from pandas DataFrame column headers](https://stackoverflow.com/a/55491499/4909087)   
 


## Cookbook





