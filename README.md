A compilation of all my canonical posts and answers to old questions on Stack Overflow, in no particular order.


## Canonicals
Meant to serve as duplicate targets for new questions.

- [Pandas Merging 101](https://stackoverflow.com/questions/53645882/pandas-merging-101)      
A primer on merging.

- [How do I slice or filter MultiIndex DataFrame levels?](https://stackoverflow.com/questions/53927460/select-rows-in-pandas-multiindex-dataframe)    
A brief writeup on how to filter MultiIndex DataFrame index or columns by label, slice, etc.

- [Performant cartesian product (CROSS JOIN) with pandas](https://stackoverflow.com/questions/53699012/performant-cartesian-product-cross-join-with-pandas)     
Performant alternatives for performing a cartesian product with pandas.

- [Fast punctuation removal with pandas](https://stackoverflow.com/questions/50444346/fast-punctuation-removal-with-pandas)     
Removing punctuation from string columns using python's silver bullet - `str.translate`.

- [What is the difference between Series.replace and Series.str.replace?](https://stackoverflow.com/questions/56625031/what-is-the-difference-between-series-replace-and-series-str-replace)    
Discuss the three main differences between `replace()` and `str.replace()`. 

## Lemmas
Augmenting your answers with helpful information without having to repeat yourself every time.

- [Creating an empty Pandas DataFrame, then filling it?](https://stackoverflow.com/a/56746204/4909087)    
I explain why this is a bad thing, and what you should instead be doing when initialising a DataFrame from ground-up.

- [How to iterate over rows in a DataFrame in Pandas?](https://stackoverflow.com/a/55557758)       
Answer: Don't.

- [For loops with pandas - When should I care?](https://stackoverflow.com/questions/54028199/for-loops-with-pandas-when-should-i-care)     
A brief writeup about the situations where for loops and iterative routines outperform pandas.

- [When should I ever want to use pandas apply() in my code?](https://stackoverflow.com/questions/54432583/when-should-i-ever-want-to-use-pandas-apply-in-my-code)    
Understanding when apply is bad and when it is not. See both answers for the full picture.

- [Dynamic Expression Evaluation in pandas using pd.eval()](https://stackoverflow.com/questions/53779986/dynamic-expression-evaluation-in-pandas-using-pd-eval)     
A brief primer on the `eval` and `query` family of functions and how they can effectively be used for dynamically evaluating expressions.

## Comprehensive Answers to Older Questions
Upto date answers to old questions, also appropriate as closure targets.

- [Understanding inplace=True](https://stackoverflow.com/a/59242208/4909087)     
Explains what `inplace=True` is, what it does, and why it should be avoided.

- [Split (explode) pandas dataframe string entry to separate rows](https://stackoverflow.com/a/57122617/4909087) and [Pandas column of lists, create a row for each list element](https://stackoverflow.com/a/57122831/4909087)    
Introducing the new `df.explode()` function (pandas >= 0.25) for exploding a column of lists into multiple rows!

- [Multiple aggregations of the same column using pandas GroupBy.agg()](https://stackoverflow.com/a/54300159)         
How to perform multiple aggregations of the same column inside GroupBy.agg, and how to rename the output columns using the new Named Aggregation API (pandas >= 0.25). 

- [Drop rows containing empty cells from a pandas DataFrame](https://stackoverflow.com/a/56708633/4909087)        
Boolean falsy filtering method, with performance comparison. `df[df['col'].astype(bool)]` happens to be faster than `df.replace({'col': {'': np.nan}}).dropna(subset=['col'])`.

- [How to get rid of “Unnamed: 0” column in a pandas DataFrame?](https://stackoverflow.com/a/54358758/4909087)      
Additional options, how to avoid having this problem manifest (don't save a `RangeIndex` to a CSV).

- [How to check if any value is NaN in a Pandas DataFrame](https://stackoverflow.com/a/53862445/4909087)    
Some extra options. Also includes `isna().any(axis=None)` (introduced in v0.23).

- [Difference between map, applymap and apply methods in Pandas](https://stackoverflow.com/a/56300992/4909087)    
A table detailing some of the most important differences between the 3 functions.

- [Writing a pandas DataFrame to CSV file](https://stackoverflow.com/a/56241457/4909087)    
A description of some of the most important arguments of `DataFrame.to_csv` and when to use them.

- [Pandas GroupBy.apply method duplicates first group](https://stackoverflow.com/a/56215416/4909087)        
Updated answer for v0.25 - `GroupBy.apply` no longer does this.

- [Import CSV file as a pandas DataFrame](https://stackoverflow.com/a/56231664/4909087)    
A description of some of the most important arguments of `pd.read_csv` and when to use them.

- [How to lowercase a pandas dataframe string column if it has missing values?](https://stackoverflow.com/a/56084317/4909087)    
Update to use `str.casefold` from v0.25 onwards.

- [Get statistics for each group (such as count, mean, etc) using pandas GroupBy?](https://stackoverflow.com/a/55564299)    
Updated to include `describe`.

- [How to implement 'in' and 'not in' for Pandas dataframe](https://stackoverflow.com/a/55554709)    
More details; `isin` on multiple columns; alternatives.

- [How to deal with SettingWithCopyWarning in Pandas?](https://stackoverflow.com/a/53954986)    
Details the causes and fixes (good, and bad) for the `SettingWithCopyWarning` in pandas. 

- [Convert list of dictionaries to a pandas DataFrame](https://stackoverflow.com/a/53831756)    

- [String concatenation of two pandas columns](https://stackoverflow.com/a/54298586)    
Various methods of joining two pandas string columns (with separator), with timings.

- [Find the max of two or more columns with pandas](https://stackoverflow.com/a/54299629)    
Fast NumPy solutions for finding the row-wise max.

- [Sorting a pandas series](https://stackoverflow.com/a/54299881)    


- [Sorting by absolute value without changing the data](https://stackoverflow.com/a/54299995)    

- [Combine duplicated columns within a DataFrame](https://stackoverflow.com/a/54300430)    
Dropping duplicate columns with the same name. 

- [Remove unwanted parts from strings in a column](https://stackoverflow.com/a/54302517)    
Removing substrings using a pattern or regex.

- [GroupBy pandas DataFrame and select most common value](https://stackoverflow.com/a/54304691)    
Find the mode using pandas GroupBy. Recent versions allow you to use `pd.Series.mode`.

- [Select rows by partial string match in index](https://stackoverflow.com/a/54314677)    
Details string methods that are available for `Index` objects.


- [Deleting all columns except a few](https://stackoverflow.com/a/54315757)    


- [How do I convert a pandas column or index to a Numpy array?](https://stackoverflow.com/a/54324513)      
Extract the underlying NumPy array or list from a Series/Index — Updated for the latest version of pandas (using `array` and `to_numpy()`).

- [Convert pandas dataframe to NumPy array](https://stackoverflow.com/a/54508052)        
Similar to above, use `to_numpy()`.

- [Setting DataFrame column headers to a MultiIndex](https://stackoverflow.com/a/54335583)    


- [Selecting columns from pandas MultiIndex](https://stackoverflow.com/a/54337009)    
Label based selection on columns.

- [Logical operators for boolean indexing in Pandas](https://stackoverflow.com/a/54358361)    
Explanation of vectorized `and`, `or`, `not` in pandas.

- [What is the difference between size and count in pandas?](https://stackoverflow.com/a/54364400)    

- [Append string to the start of each value in a said column of a pandas dataframe (elegantly)](https://stackoverflow.com/a/54392591)    
Performant list comprehension alternatives to pandas string methods.

- ['DataFrame' object has no attribute 'sort'](https://stackoverflow.com/a/54399214)    
Sorting primer 101 with the new `sort_values` API.

- [Python pandas insert list into a cell](https://stackoverflow.com/a/54399996)    
More idiomatic alternatives for pandas in 2019.

- [How to add a suffix (or prefix) to each column name?](https://stackoverflow.com/a/54410631)    
Draw a distinction between cheaper in-place assignment v/s copy in method chaining.

- [Python Pandas Create New Column with Groupby().Sum()](https://stackoverflow.com/a/54417351)    
Interesting alternative to `transform` using map

- [Select by partial string from a pandas DataFrame](https://stackoverflow.com/a/55335207)      
Address alternative implications of the title; alternative methods to `str.contains`; performance comparison.

- [How do I get the row count of a Pandas dataframe?](https://stackoverflow.com/a/55435185)      
Juxtapose various operations against their recommended methods, in tabular format.

- [What is the performance impact of non-unique indexes in pandas?](https://stackoverflow.com/a/54317984)        
Measuring the impact of sorted order and uniqueness in pandas indexes.

- [Rename a specific column in pandas](https://stackoverflow.com/a/46146667)    
More info on `rename` (with new `axis` parameter), `str.replace`, and `set_axis`

- [How to get number of groups in a groupby object in pandas?](https://stackoverflow.com/a/46512052)      

- [Convert pandas.Series from dtype object to float, and errors to nans](https://stackoverflow.com/a/47942854)      
Canonical on `pd.to_numeric` with Series and DataFrame objects.

- [How to replace values with None in Pandas data frame in Python?](https://stackoverflow.com/a/55469393)        
Nipping the problem at the bud: Read invalid values as NaN using the `na_values` attribute with the `read_csv` family of functions.

- [Get list from pandas DataFrame column headers](https://stackoverflow.com/a/55491499/4909087)    
Added some concise solutions that use iterable unpacking (introduced in python3.5).

- [Get first letter of a string from column](https://stackoverflow.com/a/55532764)        
Canonicalized version of accepted answer with timings.


