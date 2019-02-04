A compilation of all my canonical posts and answers to old questions on Stack Overflow, in no particular order.


### Canonicals
Meant to serve as duplicate targets for new questions.

- [Pandas Merging 101](https://stackoverflow.com/questions/53645882/pandas-merging-101)        
A primer on merging.

- [How do I slice or filter MultiIndex DataFrame levels?](https://stackoverflow.com/q/53927460/4909087)     
A brief writeup on how to filter MultiIndex DataFrame index or columns by label, slice, etc.

- [Performant cartesian product (CROSS JOIN) with pandas](https://stackoverflow.com/questions/53699012/performant-cartesian-product-cross-join-with-pandas)     
Performant alternatives for performing a cartesian product with pandas.

- [Fast punctuation removal with pandas](https://stackoverflow.com/q/50444346/4909087)     
Removing punctuation from string columns using python's silver bullet - `str.translate`.

### Lemmas
Augmenting your answers with helpful information without having to repeat yourself every time.

- [For loops with pandas - When should I care?](https://stackoverflow.com/questions/54028199/for-loops-with-pandas-when-should-i-care)     
A brief writeup about the situations where for loops and iterative routines outperform pandas.

- [When should I ever want to use pandas apply() in my code?](https://stackoverflow.com/q/54432583/4909087)    
Understanding when apply is bad and when it is not. See both answers for the full picture.

- [Dynamic Expression Evaluation in pandas using pd.eval()](https://stackoverflow.com/q/53779986/4909087)     
A brief primer on the `eval` and `query` family of functions and how they can effectively be used for dynamically evaluating expressions.

### Comprehensive Answers to Older Questions
Upto date answers to old questions, also appropriate as closure targets.

- [How to deal with SettingWithCopyWarning in Pandas?](https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas/53954986#53954986)    
Details the causes and fixes (good, and bad) for the `SettingWithCopyWarning` in pandas. 

- [Convert list of dictionaries to a pandas DataFrame](https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe/53831756#53831756)    

- [Redefining the Index in a Pandas DataFrame object](https://stackoverflow.com/questions/10457584/redefining-the-index-in-a-pandas-dataframe-object/54297213#54297213)    
How to set the index of a DataFrame to something else.

- [String concatenation of two pandas columns](https://stackoverflow.com/questions/11858472/string-concatenation-of-two-pandas-columns/54298586#54298586)    
Joining two pandas string columns (with separator), with performance comparison.

- [Find the max of two or more columns with pandas](https://stackoverflow.com/questions/12169170/find-the-max-of-two-or-more-columns-with-pandas/54299629#54299629)    
Fast NumPy solutions for finding the row-wise max.

- [Sorting a pandas series](https://stackoverflow.com/questions/12133075/sorting-a-pandas-series/54299881#54299881)    


- [Sorting by absolute value without changing the data](https://stackoverflow.com/questions/30486263/sorting-by-absolute-value-without-changing-the-data/54299995#54299995)    


- [Multiple aggregations of the same column using pandas GroupBy.agg()](https://stackoverflow.com/questions/12589481/multiple-aggregations-of-the-same-column-using-pandas-groupby-agg/54300159#54300159)    
How to perform multiple aggregations of the same column inside GroupBy.agg, and how to rename the output columns.

- [Combine duplicated columns within a DataFrame](https://stackoverflow.com/questions/13078751/combine-duplicated-columns-within-a-dataframe/54300430#54300430)    
Dropping duplicate columns with the same name. 

- [Remove unwanted parts from strings in a column](https://stackoverflow.com/questions/13682044/remove-unwanted-parts-from-strings-in-a-column/54302517#54302517)    
Removing substrings using a pattern or regex.

- [GroupBy pandas DataFrame and select most common value](https://stackoverflow.com/questions/15222754/groupby-pandas-dataframe-and-select-most-common-value/54304691#54304691)    
Find the mode using pandas GroupBy. Recent versions allow you to use `pd.Series.mode`.

- [Select rows by partial string match in index](https://stackoverflow.com/questions/16617394/select-rows-by-partial-string-match-in-index/54314677#54314677)    
Details string methods that are available for `Index` objects.


- [Deleting all columns except a few](https://stackoverflow.com/questions/16616141/deleting-all-columns-except-a-few-python-pandas/54315757#54315757)    

- [Replace string/value in entire DataFrame](https://stackoverflow.com/questions/17142304/replace-string-value-in-entire-dataframe/54322615#54322615)    
Faster alternatives to `DataFrame.replace`.

- [How do I get a DataFrame Index / Series column as an array or list?](https://stackoverflow.com/questions/17241004/how-do-i-get-a-dataframe-index-series-column-as-an-array-or-list/54324513#54324513)      
Extract the underlying NumPy array or list from a Series/Index — Updated for the latest version of pandas (using `array` and `to_numpy()`).

- [Convert pandas dataframe to NumPy array](https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array/54508052#54508052)        
Similar to above, use `to_numpy()`.

- [Setting DataFrame column headers to a MultiIndex](https://stackoverflow.com/questions/18262962/setting-dataframe-column-headers-to-a-multiindex/54335583#54335583)    


- [Selecting columns from pandas MultiIndex](https://stackoverflow.com/questions/18470323/selecting-columns-from-pandas-multiindex/54337009#54337009)    
Label based selection on columns.

- [Get particular row as series from pandas dataframe](https://stackoverflow.com/questions/19599578/get-particular-row-as-series-from-pandas-dataframe/54344511#54344511)    
The most appropriate method of extracting a single row as a Series.

- [Logical operators for boolean indexing in Pandas](https://stackoverflow.com/a/54358361/4909087)    
Explanation of vectorized `and`, `or`, `not` in pandas.

- [What is the difference between size and count in pandas?](https://stackoverflow.com/a/54364400/4909087)    

- [Append string to the start of each value in a said column of a pandas dataframe (elegantly)](https://stackoverflow.com/a/54392591/4909087)    
Performant list comprehension alternatives to pandas string methods.

- ['DataFrame' object has no attribute 'sort'](https://stackoverflow.com/a/54399214/4909087)    
Sorting primer 101 with the new `sort_values` API.

- [Python pandas insert list into a cell](https://stackoverflow.com/questions/26483254/python-pandas-insert-list-into-a-cell/54399996#54399996)    
More idiomatic alternatives for pandas in 2019.

- [How to add a suffix (or prefix) to each column name?](https://stackoverflow.com/a/54410631/4909087)    
Draw a distinction between cheaper in-place assignment v/s copy in method chaining.

- [Python Pandas Create New Column with Groupby().Sum()](https://stackoverflow.com/a/54417351/4909087)    
Interesting alternative to `transform` using map

- [Get last “column” after .str.split() operation on column in pandas DataFrame](https://stackoverflow.com/a/54457389/4909087)    
Vectorized string and list comprehension methods.


- (Python question) [Check if something is not in a list in Python](https://stackoverflow.com/a/54437309/4909087)
