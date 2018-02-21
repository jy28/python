Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> url
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    url
NameError: name 'url' is not defined
>>> url = "https:// archive.ics.uci.edu/ml/machine-learning-databases/autos/imprts-85.data"
>>> df = pd.read_csv(url, header =none)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    df = pd.read_csv(url, header =none)
NameError: name 'none' is not defined
>>> df=pd.read_csv(url)
Traceback (most recent call last):
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1026, in _send_output
    self.send(msg)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 964, in send
    self.connect()
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 1392, in connect
    super().connect()
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\http\client.py", line 936, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 704, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\socket.py", line 745, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df=pd.read_csv(url)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 709, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\parsers.py", line 433, in _read
    filepath_or_buffer, encoding, compression)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\io\common.py", line 190, in get_filepath_or_buffer
    req = _urlopen(filepath_or_buffer)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 526, in open
    response = self._open(req, data)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 544, in _open
    '_open', req)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 504, in _call_chain
    result = func(*args)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Users\Jyoti\AppData\Local\Programs\Python\Python36-32\lib\urllib\request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
>>> df=pd.read_csv(url)

>>> df
     3    ?  alfa-romero     gas    std   two  convertible  rwd  front  88.60  \
0    3    ?  alfa-romero     gas    std   two  convertible  rwd  front   88.6   
1    1    ?  alfa-romero     gas    std   two    hatchback  rwd  front   94.5   
2    2  164         audi     gas    std  four        sedan  fwd  front   99.8   
3    2  164         audi     gas    std  four        sedan  4wd  front   99.4   
4    2    ?         audi     gas    std   two        sedan  fwd  front   99.8   
5    1  158         audi     gas    std  four        sedan  fwd  front  105.8   
6    1    ?         audi     gas    std  four        wagon  fwd  front  105.8   
7    1  158         audi     gas  turbo  four        sedan  fwd  front  105.8   
8    0    ?         audi     gas  turbo   two    hatchback  4wd  front   99.5   
9    2  192          bmw     gas    std   two        sedan  rwd  front  101.2   
10   0  192          bmw     gas    std  four        sedan  rwd  front  101.2   
11   0  188          bmw     gas    std   two        sedan  rwd  front  101.2   
12   0  188          bmw     gas    std  four        sedan  rwd  front  101.2   
13   1    ?          bmw     gas    std  four        sedan  rwd  front  103.5   
14   0    ?          bmw     gas    std  four        sedan  rwd  front  103.5   
15   0    ?          bmw     gas    std   two        sedan  rwd  front  103.5   
16   0    ?          bmw     gas    std  four        sedan  rwd  front  110.0   
17   2  121    chevrolet     gas    std   two    hatchback  fwd  front   88.4   
18   1   98    chevrolet     gas    std   two    hatchback  fwd  front   94.5   
19   0   81    chevrolet     gas    std  four        sedan  fwd  front   94.5   
20   1  118        dodge     gas    std   two    hatchback  fwd  front   93.7   
21   1  118        dodge     gas    std   two    hatchback  fwd  front   93.7   
22   1  118        dodge     gas  turbo   two    hatchback  fwd  front   93.7   
23   1  148        dodge     gas    std  four    hatchback  fwd  front   93.7   
24   1  148        dodge     gas    std  four        sedan  fwd  front   93.7   
25   1  148        dodge     gas    std  four        sedan  fwd  front   93.7   
26   1  148        dodge     gas  turbo     ?        sedan  fwd  front   93.7   
27  -1  110        dodge     gas    std  four        wagon  fwd  front  103.3   
28   3  145        dodge     gas  turbo   two    hatchback  fwd  front   95.9   
29   2  137        honda     gas    std   two    hatchback  fwd  front   86.6   
..  ..  ...          ...     ...    ...   ...          ...  ...    ...    ...   
174 -1   65       toyota     gas    std  four    hatchback  fwd  front  102.4   
175 -1   65       toyota     gas    std  four        sedan  fwd  front  102.4   
176 -1   65       toyota     gas    std  four    hatchback  fwd  front  102.4   
177  3  197       toyota     gas    std   two    hatchback  rwd  front  102.9   
178  3  197       toyota     gas    std   two    hatchback  rwd  front  102.9   
179 -1   90       toyota     gas    std  four        sedan  rwd  front  104.5   
180 -1    ?       toyota     gas    std  four        wagon  rwd  front  104.5   
181  2  122   volkswagen  diesel    std   two        sedan  fwd  front   97.3   
182  2  122   volkswagen     gas    std   two        sedan  fwd  front   97.3   
183  2   94   volkswagen  diesel    std  four        sedan  fwd  front   97.3   
184  2   94   volkswagen     gas    std  four        sedan  fwd  front   97.3   
185  2   94   volkswagen     gas    std  four        sedan  fwd  front   97.3   
186  2   94   volkswagen  diesel  turbo  four        sedan  fwd  front   97.3   
187  2   94   volkswagen     gas    std  four        sedan  fwd  front   97.3   
188  3    ?   volkswagen     gas    std   two  convertible  fwd  front   94.5   
189  3  256   volkswagen     gas    std   two    hatchback  fwd  front   94.5   
190  0    ?   volkswagen     gas    std  four        sedan  fwd  front  100.4   
191  0    ?   volkswagen  diesel  turbo  four        sedan  fwd  front  100.4   
192  0    ?   volkswagen     gas    std  four        wagon  fwd  front  100.4   
193 -2  103        volvo     gas    std  four        sedan  rwd  front  104.3   
194 -1   74        volvo     gas    std  four        wagon  rwd  front  104.3   
195 -2  103        volvo     gas    std  four        sedan  rwd  front  104.3   
196 -1   74        volvo     gas    std  four        wagon  rwd  front  104.3   
197 -2  103        volvo     gas  turbo  four        sedan  rwd  front  104.3   
198 -1   74        volvo     gas  turbo  four        wagon  rwd  front  104.3   
199 -1   95        volvo     gas    std  four        sedan  rwd  front  109.1   
200 -1   95        volvo     gas  turbo  four        sedan  rwd  front  109.1   
201 -1   95        volvo     gas    std  four        sedan  rwd  front  109.1   
202 -1   95        volvo  diesel  turbo  four        sedan  rwd  front  109.1   
203 -1   95        volvo     gas  turbo  four        sedan  rwd  front  109.1   

     ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  13495  
0    ...    130  mpfi  3.47  2.68   9.00  111  5000  21  27  16500  
1    ...    152  mpfi  2.68  3.47   9.00  154  5000  19  26  16500  
2    ...    109  mpfi  3.19  3.40  10.00  102  5500  24  30  13950  
3    ...    136  mpfi  3.19  3.40   8.00  115  5500  18  22  17450  
4    ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  15250  
5    ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  17710  
6    ...    136  mpfi  3.19  3.40   8.50  110  5500  19  25  18920  
7    ...    131  mpfi  3.13  3.40   8.30  140  5500  17  20  23875  
8    ...    131  mpfi  3.13  3.40   7.00  160  5500  16  22      ?  
9    ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16430  
10   ...    108  mpfi  3.50  2.80   8.80  101  5800  23  29  16925  
11   ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  20970  
12   ...    164  mpfi  3.31  3.19   9.00  121  4250  21  28  21105  
13   ...    164  mpfi  3.31  3.19   9.00  121  4250  20  25  24565  
14   ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  30760  
15   ...    209  mpfi  3.62  3.39   8.00  182  5400  16  22  41315  
16   ...    209  mpfi  3.62  3.39   8.00  182  5400  15  20  36880  
17   ...     61  2bbl  2.91  3.03   9.50   48  5100  47  53   5151  
18   ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6295  
19   ...     90  2bbl  3.03  3.11   9.60   70  5400  38  43   6575  
20   ...     90  2bbl  2.97  3.23   9.41   68  5500  37  41   5572  
21   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6377  
22   ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   7957  
23   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6229  
24   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   6692  
25   ...     90  2bbl  2.97  3.23   9.40   68  5500  31  38   7609  
26   ...     98  mpfi  3.03  3.39   7.60  102  5500  24  30   8558  
27   ...    122  2bbl  3.34  3.46   8.50   88  5000  24  30   8921  
28   ...    156   mfi  3.60  3.90   7.00  145  5000  19  24  12964  
29   ...     92  1bbl  2.91  3.41   9.60   58  4800  49  54   6479  
..   ...    ...   ...   ...   ...    ...  ...   ...  ..  ..    ...  
174  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32   9988  
175  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  10898  
176  ...    122  mpfi  3.31  3.54   8.70   92  4200  27  32  11248  
177  ...    171  mpfi  3.27  3.35   9.30  161  5200  20  24  16558  
178  ...    171  mpfi  3.27  3.35   9.30  161  5200  19  24  15998  
179  ...    171  mpfi  3.27  3.35   9.20  156  5200  20  24  15690  
180  ...    161  mpfi  3.27  3.35   9.20  156  5200  19  24  15750  
181  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7775  
182  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   7975  
183  ...     97   idi  3.01  3.40  23.00   52  4800  37  46   7995  
184  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8195  
185  ...    109  mpfi  3.19  3.40   9.00   85  5250  27  34   8495  
186  ...     97   idi  3.01  3.40  23.00   68  4500  37  42   9495  
187  ...    109  mpfi  3.19  3.40  10.00  100  5500  26  32   9995  
188  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29  11595  
189  ...    109  mpfi  3.19  3.40   8.50   90  5500  24  29   9980  
190  ...    136  mpfi  3.19  3.40   8.50  110  5500  19  24  13295  
191  ...     97   idi  3.01  3.40  23.00   68  4500  33  38  13845  
192  ...    109  mpfi  3.19  3.40   9.00   88  5500  25  31  12290  
193  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  12940  
194  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  13415  
195  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  15985  
196  ...    141  mpfi  3.78  3.15   9.50  114  5400  24  28  16515  
197  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18420  
198  ...    130  mpfi  3.62  3.15   7.50  162  5100  17  22  18950  
199  ...    141  mpfi  3.78  3.15   9.50  114  5400  23  28  16845  
200  ...    141  mpfi  3.78  3.15   8.70  160  5300  19  25  19045  
201  ...    173  mpfi  3.58  2.87   8.80  134  5500  18  23  21485  
202  ...    145   idi  3.01  3.40  23.00  106  4800  26  27  22470  
203  ...    141  mpfi  3.78  3.15   9.50  114  5400  19  25  22625  

[204 rows x 26 columns]
>>> headers=["symboling","normalized-
losses","make","fuel-
type","aspiration","num-of-
doors","body-style","drive-
wheels","engine-location","wheel-
base","lenght","width","height","curb-
weight","engine-type","num-of -
cylinders","engine-size","fuel-
system","bore","stroke","compression-
ratio","horsepower","peak-rpm","city-
mpg","highway-mpg","price"]
	     
SyntaxError: EOL while scanning string literal
>>> headers=["symboling","normalized-
losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","lenght","width","height","curb-weight","engine-type","num-of -cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
	     
SyntaxError: EOL while scanning string literal
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","lenght","width","height","curb-weight","engine-type","num-of -cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
	     
SyntaxError: EOL while scanning string literal
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","lenght","width","height","curb-weight","engine-type","num-of -cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
	     
SyntaxError: EOL while scanning string literal
>>> headers=["symboling","normalized_losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","lenght","width","height","curb-weight","engine-type","num-of -cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
	     
SyntaxError: EOL while scanning string literal
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","lenght","width","height","curb-weight","engine-type","num-of -cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
	     
SyntaxError: EOL while scanning string literal
>>> 
	     
>>> headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","lenght","width","height","curb-weight","engine-type","num-of -cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"]
	     
>>> df.columns=headers
	     
>>> df
	     
     symboling normalized-losses         make fuel-type aspiration  \
0            3                 ?  alfa-romero       gas        std   
1            1                 ?  alfa-romero       gas        std   
2            2               164         audi       gas        std   
3            2               164         audi       gas        std   
4            2                 ?         audi       gas        std   
5            1               158         audi       gas        std   
6            1                 ?         audi       gas        std   
7            1               158         audi       gas      turbo   
8            0                 ?         audi       gas      turbo   
9            2               192          bmw       gas        std   
10           0               192          bmw       gas        std   
11           0               188          bmw       gas        std   
12           0               188          bmw       gas        std   
13           1                 ?          bmw       gas        std   
14           0                 ?          bmw       gas        std   
15           0                 ?          bmw       gas        std   
16           0                 ?          bmw       gas        std   
17           2               121    chevrolet       gas        std   
18           1                98    chevrolet       gas        std   
19           0                81    chevrolet       gas        std   
20           1               118        dodge       gas        std   
21           1               118        dodge       gas        std   
22           1               118        dodge       gas      turbo   
23           1               148        dodge       gas        std   
24           1               148        dodge       gas        std   
25           1               148        dodge       gas        std   
26           1               148        dodge       gas      turbo   
27          -1               110        dodge       gas        std   
28           3               145        dodge       gas      turbo   
29           2               137        honda       gas        std   
..         ...               ...          ...       ...        ...   
174         -1                65       toyota       gas        std   
175         -1                65       toyota       gas        std   
176         -1                65       toyota       gas        std   
177          3               197       toyota       gas        std   
178          3               197       toyota       gas        std   
179         -1                90       toyota       gas        std   
180         -1                 ?       toyota       gas        std   
181          2               122   volkswagen    diesel        std   
182          2               122   volkswagen       gas        std   
183          2                94   volkswagen    diesel        std   
184          2                94   volkswagen       gas        std   
185          2                94   volkswagen       gas        std   
186          2                94   volkswagen    diesel      turbo   
187          2                94   volkswagen       gas        std   
188          3                 ?   volkswagen       gas        std   
189          3               256   volkswagen       gas        std   
190          0                 ?   volkswagen       gas        std   
191          0                 ?   volkswagen    diesel      turbo   
192          0                 ?   volkswagen       gas        std   
193         -2               103        volvo       gas        std   
194         -1                74        volvo       gas        std   
195         -2               103        volvo       gas        std   
196         -1                74        volvo       gas        std   
197         -2               103        volvo       gas      turbo   
198         -1                74        volvo       gas      turbo   
199         -1                95        volvo       gas        std   
200         -1                95        volvo       gas      turbo   
201         -1                95        volvo       gas        std   
202         -1                95        volvo    diesel      turbo   
203         -1                95        volvo       gas      turbo   

    num-of-doors   body-style drive-wheels engine-location  wheel-base  ...    \
0            two  convertible          rwd           front        88.6  ...     
1            two    hatchback          rwd           front        94.5  ...     
2           four        sedan          fwd           front        99.8  ...     
3           four        sedan          4wd           front        99.4  ...     
4            two        sedan          fwd           front        99.8  ...     
5           four        sedan          fwd           front       105.8  ...     
6           four        wagon          fwd           front       105.8  ...     
7           four        sedan          fwd           front       105.8  ...     
8            two    hatchback          4wd           front        99.5  ...     
9            two        sedan          rwd           front       101.2  ...     
10          four        sedan          rwd           front       101.2  ...     
11           two        sedan          rwd           front       101.2  ...     
12          four        sedan          rwd           front       101.2  ...     
13          four        sedan          rwd           front       103.5  ...     
14          four        sedan          rwd           front       103.5  ...     
15           two        sedan          rwd           front       103.5  ...     
16          four        sedan          rwd           front       110.0  ...     
17           two    hatchback          fwd           front        88.4  ...     
18           two    hatchback          fwd           front        94.5  ...     
19          four        sedan          fwd           front        94.5  ...     
20           two    hatchback          fwd           front        93.7  ...     
21           two    hatchback          fwd           front        93.7  ...     
22           two    hatchback          fwd           front        93.7  ...     
23          four    hatchback          fwd           front        93.7  ...     
24          four        sedan          fwd           front        93.7  ...     
25          four        sedan          fwd           front        93.7  ...     
26             ?        sedan          fwd           front        93.7  ...     
27          four        wagon          fwd           front       103.3  ...     
28           two    hatchback          fwd           front        95.9  ...     
29           two    hatchback          fwd           front        86.6  ...     
..           ...          ...          ...             ...         ...  ...     
174         four    hatchback          fwd           front       102.4  ...     
175         four        sedan          fwd           front       102.4  ...     
176         four    hatchback          fwd           front       102.4  ...     
177          two    hatchback          rwd           front       102.9  ...     
178          two    hatchback          rwd           front       102.9  ...     
179         four        sedan          rwd           front       104.5  ...     
180         four        wagon          rwd           front       104.5  ...     
181          two        sedan          fwd           front        97.3  ...     
182          two        sedan          fwd           front        97.3  ...     
183         four        sedan          fwd           front        97.3  ...     
184         four        sedan          fwd           front        97.3  ...     
185         four        sedan          fwd           front        97.3  ...     
186         four        sedan          fwd           front        97.3  ...     
187         four        sedan          fwd           front        97.3  ...     
188          two  convertible          fwd           front        94.5  ...     
189          two    hatchback          fwd           front        94.5  ...     
190         four        sedan          fwd           front       100.4  ...     
191         four        sedan          fwd           front       100.4  ...     
192         four        wagon          fwd           front       100.4  ...     
193         four        sedan          rwd           front       104.3  ...     
194         four        wagon          rwd           front       104.3  ...     
195         four        sedan          rwd           front       104.3  ...     
196         four        wagon          rwd           front       104.3  ...     
197         four        sedan          rwd           front       104.3  ...     
198         four        wagon          rwd           front       104.3  ...     
199         four        sedan          rwd           front       109.1  ...     
200         four        sedan          rwd           front       109.1  ...     
201         four        sedan          rwd           front       109.1  ...     
202         four        sedan          rwd           front       109.1  ...     
203         four        sedan          rwd           front       109.1  ...     

     engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
0            130         mpfi  3.47    2.68              9.00        111   
1            152         mpfi  2.68    3.47              9.00        154   
2            109         mpfi  3.19    3.40             10.00        102   
3            136         mpfi  3.19    3.40              8.00        115   
4            136         mpfi  3.19    3.40              8.50        110   
5            136         mpfi  3.19    3.40              8.50        110   
6            136         mpfi  3.19    3.40              8.50        110   
7            131         mpfi  3.13    3.40              8.30        140   
8            131         mpfi  3.13    3.40              7.00        160   
9            108         mpfi  3.50    2.80              8.80        101   
10           108         mpfi  3.50    2.80              8.80        101   
11           164         mpfi  3.31    3.19              9.00        121   
12           164         mpfi  3.31    3.19              9.00        121   
13           164         mpfi  3.31    3.19              9.00        121   
14           209         mpfi  3.62    3.39              8.00        182   
15           209         mpfi  3.62    3.39              8.00        182   
16           209         mpfi  3.62    3.39              8.00        182   
17            61         2bbl  2.91    3.03              9.50         48   
18            90         2bbl  3.03    3.11              9.60         70   
19            90         2bbl  3.03    3.11              9.60         70   
20            90         2bbl  2.97    3.23              9.41         68   
21            90         2bbl  2.97    3.23              9.40         68   
22            98         mpfi  3.03    3.39              7.60        102   
23            90         2bbl  2.97    3.23              9.40         68   
24            90         2bbl  2.97    3.23              9.40         68   
25            90         2bbl  2.97    3.23              9.40         68   
26            98         mpfi  3.03    3.39              7.60        102   
27           122         2bbl  3.34    3.46              8.50         88   
28           156          mfi  3.60    3.90              7.00        145   
29            92         1bbl  2.91    3.41              9.60         58   
..           ...          ...   ...     ...               ...        ...   
174          122         mpfi  3.31    3.54              8.70         92   
175          122         mpfi  3.31    3.54              8.70         92   
176          122         mpfi  3.31    3.54              8.70         92   
177          171         mpfi  3.27    3.35              9.30        161   
178          171         mpfi  3.27    3.35              9.30        161   
179          171         mpfi  3.27    3.35              9.20        156   
180          161         mpfi  3.27    3.35              9.20        156   
181           97          idi  3.01    3.40             23.00         52   
182          109         mpfi  3.19    3.40              9.00         85   
183           97          idi  3.01    3.40             23.00         52   
184          109         mpfi  3.19    3.40              9.00         85   
185          109         mpfi  3.19    3.40              9.00         85   
186           97          idi  3.01    3.40             23.00         68   
187          109         mpfi  3.19    3.40             10.00        100   
188          109         mpfi  3.19    3.40              8.50         90   
189          109         mpfi  3.19    3.40              8.50         90   
190          136         mpfi  3.19    3.40              8.50        110   
191           97          idi  3.01    3.40             23.00         68   
192          109         mpfi  3.19    3.40              9.00         88   
193          141         mpfi  3.78    3.15              9.50        114   
194          141         mpfi  3.78    3.15              9.50        114   
195          141         mpfi  3.78    3.15              9.50        114   
196          141         mpfi  3.78    3.15              9.50        114   
197          130         mpfi  3.62    3.15              7.50        162   
198          130         mpfi  3.62    3.15              7.50        162   
199          141         mpfi  3.78    3.15              9.50        114   
200          141         mpfi  3.78    3.15              8.70        160   
201          173         mpfi  3.58    2.87              8.80        134   
202          145          idi  3.01    3.40             23.00        106   
203          141         mpfi  3.78    3.15              9.50        114   

     peak-rpm city-mpg highway-mpg  price  
0        5000       21          27  16500  
1        5000       19          26  16500  
2        5500       24          30  13950  
3        5500       18          22  17450  
4        5500       19          25  15250  
5        5500       19          25  17710  
6        5500       19          25  18920  
7        5500       17          20  23875  
8        5500       16          22      ?  
9        5800       23          29  16430  
10       5800       23          29  16925  
11       4250       21          28  20970  
12       4250       21          28  21105  
13       4250       20          25  24565  
14       5400       16          22  30760  
15       5400       16          22  41315  
16       5400       15          20  36880  
17       5100       47          53   5151  
18       5400       38          43   6295  
19       5400       38          43   6575  
20       5500       37          41   5572  
21       5500       31          38   6377  
22       5500       24          30   7957  
23       5500       31          38   6229  
24       5500       31          38   6692  
25       5500       31          38   7609  
26       5500       24          30   8558  
27       5000       24          30   8921  
28       5000       19          24  12964  
29       4800       49          54   6479  
..        ...      ...         ...    ...  
174      4200       27          32   9988  
175      4200       27          32  10898  
176      4200       27          32  11248  
177      5200       20          24  16558  
178      5200       19          24  15998  
179      5200       20          24  15690  
180      5200       19          24  15750  
181      4800       37          46   7775  
182      5250       27          34   7975  
183      4800       37          46   7995  
184      5250       27          34   8195  
185      5250       27          34   8495  
186      4500       37          42   9495  
187      5500       26          32   9995  
188      5500       24          29  11595  
189      5500       24          29   9980  
190      5500       19          24  13295  
191      4500       33          38  13845  
192      5500       25          31  12290  
193      5400       23          28  12940  
194      5400       23          28  13415  
195      5400       24          28  15985  
196      5400       24          28  16515  
197      5100       17          22  18420  
198      5100       17          22  18950  
199      5400       23          28  16845  
200      5300       19          25  19045  
201      5500       18          23  21485  
202      4800       26          27  22470  
203      5400       19          25  22625  

[204 rows x 26 columns]
>>> df.head(5)
	     
   symboling normalized-losses         make fuel-type aspiration num-of-doors  \
0          3                 ?  alfa-romero       gas        std          two   
1          1                 ?  alfa-romero       gas        std          two   
2          2               164         audi       gas        std         four   
3          2               164         audi       gas        std         four   
4          2                 ?         audi       gas        std          two   

    body-style drive-wheels engine-location  wheel-base  ...    engine-size  \
0  convertible          rwd           front        88.6  ...            130   
1    hatchback          rwd           front        94.5  ...            152   
2        sedan          fwd           front        99.8  ...            109   
3        sedan          4wd           front        99.4  ...            136   
4        sedan          fwd           front        99.8  ...            136   

   fuel-system  bore  stroke compression-ratio horsepower  peak-rpm city-mpg  \
0         mpfi  3.47    2.68               9.0        111      5000       21   
1         mpfi  2.68    3.47               9.0        154      5000       19   
2         mpfi  3.19    3.40              10.0        102      5500       24   
3         mpfi  3.19    3.40               8.0        115      5500       18   
4         mpfi  3.19    3.40               8.5        110      5500       19   

  highway-mpg  price  
0          27  16500  
1          26  16500  
2          30  13950  
3          22  17450  
4          25  15250  

[5 rows x 26 columns]
>>> 
