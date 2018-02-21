Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plot
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates = pd.date_range('20130101', periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

>>> df
                   A         B         C         D
2013-01-01  0.178477 -1.255501  2.340031  1.841436
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
2013-01-05 -0.488823 -0.240937 -1.035238 -0.584244
2013-01-06  0.244861  0.120818  0.852170  0.786745
>>> df2 = pd.DataFrame({ 'A' : 1.,
			 'B' : pd.Timestamp('20130102'),
			 'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
			 'E' : pd.Categorical(["test","train","test","train"]),
			 'F' : 'foo' })
>>> df2
     A          B    C      E    F
0  1.0 2013-01-02  1.0   test  foo
1  1.0 2013-01-02  1.0  train  foo
2  1.0 2013-01-02  1.0   test  foo
3  1.0 2013-01-02  1.0  train  foo
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
E          category
F            object
dtype: object
>>> df2.<TAB>
SyntaxError: invalid syntax
>>> df.head()
                   A         B         C         D
2013-01-01  0.178477 -1.255501  2.340031  1.841436
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
2013-01-05 -0.488823 -0.240937 -1.035238 -0.584244
>>> df.tail(3)
                   A         B         C         D
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
2013-01-05 -0.488823 -0.240937 -1.035238 -0.584244
2013-01-06  0.244861  0.120818  0.852170  0.786745
>>> df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> df.columns
Index(['A', 'B', 'C', 'D'], dtype='object')
>>> df.values
array([[ 0.17847736, -1.2555009 ,  2.34003088,  1.84143623],
       [ 1.76578225, -0.29266675, -0.51224625,  0.48552914],
       [-1.02584105, -0.51245913,  1.45994894, -0.47732422],
       [ 0.54295117, -1.76635848, -0.26947911,  1.00890477],
       [-0.48882292, -0.24093735, -1.03523828, -0.58424379],
       [ 0.24486104,  0.12081778,  0.85216987,  0.78674453]])
>>> df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.202901 -0.657851  0.472531  0.510174
std    0.953822  0.710016  1.296180  0.924229
min   -1.025841 -1.766358 -1.035238 -0.584244
25%   -0.321998 -1.069740 -0.451554 -0.236611
50%    0.211669 -0.402563  0.291345  0.636137
75%    0.468429 -0.253870  1.308004  0.953365
max    1.765782  0.120818  2.340031  1.841436
>>> df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.178477    1.765782   -1.025841    0.542951   -0.488823    0.244861
B   -1.255501   -0.292667   -0.512459   -1.766358   -0.240937    0.120818
C    2.340031   -0.512246    1.459949   -0.269479   -1.035238    0.852170
D    1.841436    0.485529   -0.477324    1.008905   -0.584244    0.786745
>>> df.sort_index(axis=1, ascending=False)

                   D         C         B         A
2013-01-01  1.841436  2.340031 -1.255501  0.178477
2013-01-02  0.485529 -0.512246 -0.292667  1.765782
2013-01-03 -0.477324  1.459949 -0.512459 -1.025841
2013-01-04  1.008905 -0.269479 -1.766358  0.542951
2013-01-05 -0.584244 -1.035238 -0.240937 -0.488823
2013-01-06  0.786745  0.852170  0.120818  0.244861
>>> df.sort_values(by='B')
                   A         B         C         D
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
2013-01-01  0.178477 -1.255501  2.340031  1.841436
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-05 -0.488823 -0.240937 -1.035238 -0.584244
2013-01-06  0.244861  0.120818  0.852170  0.786745
>>> 
KeyboardInterrupt
>>> df['A']
2013-01-01    0.178477
2013-01-02    1.765782
2013-01-03   -1.025841
2013-01-04    0.542951
2013-01-05   -0.488823
2013-01-06    0.244861
Freq: D, Name: A, dtype: float64
>>> df[0:3]
                   A         B         C         D
2013-01-01  0.178477 -1.255501  2.340031  1.841436
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
>>> df['20130102':'20130104']
                   A         B         C         D
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
>>> df.loc[dates[0]]
A    0.178477
B   -1.255501
C    2.340031
D    1.841436
Name: 2013-01-01 00:00:00, dtype: float64
>>> df.loc[:,['A','B']]
                   A         B
2013-01-01  0.178477 -1.255501
2013-01-02  1.765782 -0.292667
2013-01-03 -1.025841 -0.512459
2013-01-04  0.542951 -1.766358
2013-01-05 -0.488823 -0.240937
2013-01-06  0.244861  0.120818
>>>  df.loc['20130102':'20130104',['A','B']]
SyntaxError: unexpected indent
>>> df.loc['20130102':'20130104',['A','B']]
                   A         B
2013-01-02  1.765782 -0.292667
2013-01-03 -1.025841 -0.512459
2013-01-04  0.542951 -1.766358
>>> df.loc['20130102',['A','B']]
A    1.765782
B   -0.292667
Name: 2013-01-02 00:00:00, dtype: float64
>>> df.loc[dates[0],'A']
0.17847735750648572
>>> df.at[dates[0],'A']
0.17847735750648572
>>> df.iloc[3]
A    0.542951
B   -1.766358
C   -0.269479
D    1.008905
Name: 2013-01-04 00:00:00, dtype: float64
>>> df.iloc[3:5,0:2]
                   A         B
2013-01-04  0.542951 -1.766358
2013-01-05 -0.488823 -0.240937
>>> df.iloc[[1,2,4],[0,2]]
                   A         C
2013-01-02  1.765782 -0.512246
2013-01-03 -1.025841  1.459949
2013-01-05 -0.488823 -1.035238
>>> df.iloc[1:3,:]
                   A         B         C         D
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
>>> df.iloc[:,1:3]
                   B         C
2013-01-01 -1.255501  2.340031
2013-01-02 -0.292667 -0.512246
2013-01-03 -0.512459  1.459949
2013-01-04 -1.766358 -0.269479
2013-01-05 -0.240937 -1.035238
2013-01-06  0.120818  0.852170
>>> df.iloc[1,1]
-0.29266675040213874
>>> df.iat[1,1]
-0.29266675040213874
>>>  df[df.A > 0]
SyntaxError: unexpected indent
>>> df[df.A > 0]
                   A         B         C         D
2013-01-01  0.178477 -1.255501  2.340031  1.841436
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
2013-01-06  0.244861  0.120818  0.852170  0.786745
>>> df[df > 0]
                   A         B         C         D
2013-01-01  0.178477       NaN  2.340031  1.841436
2013-01-02  1.765782       NaN       NaN  0.485529
2013-01-03       NaN       NaN  1.459949       NaN
2013-01-04  0.542951       NaN       NaN  1.008905
2013-01-05       NaN       NaN       NaN       NaN
2013-01-06  0.244861  0.120818  0.852170  0.786745
>>> df2 = df.copy()
>>> df2
                   A         B         C         D
2013-01-01  0.178477 -1.255501  2.340031  1.841436
2013-01-02  1.765782 -0.292667 -0.512246  0.485529
2013-01-03 -1.025841 -0.512459  1.459949 -0.477324
2013-01-04  0.542951 -1.766358 -0.269479  1.008905
2013-01-05 -0.488823 -0.240937 -1.035238 -0.584244
2013-01-06  0.244861  0.120818  0.852170  0.786745
>>> df2[df2['E'].isin(['two','four'])]
Traceback (most recent call last):
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 2525, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'E'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    df2[df2['E'].isin(['two','four'])]
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 2139, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 2146, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 1842, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3843, in get
    loc = self.items.get_loc(item)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 2527, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'E'
>>>  df2[df2['E'].isin(['two','four'])]
SyntaxError: unexpected indent
>>> df2[df2['E'].isin(['two','four'])]
Traceback (most recent call last):
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 2525, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'E'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    df2[df2['E'].isin(['two','four'])]
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 2139, in __getitem__
    return self._getitem_column(key)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\frame.py", line 2146, in _getitem_column
    return self._get_item_cache(key)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 1842, in _get_item_cache
    values = self._data.get(item)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\internals.py", line 3843, in get
    loc = self.items.get_loc(item)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\indexes\base.py", line 2527, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 117, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 139, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1265, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1273, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'E'
>>> 
