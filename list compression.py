Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> matrix = [
	[1,2,3,4],
	[5,6,7,8,],
	[9,10,11,12],
	]
>>> [[row[i] for row in matrix] for i in range (4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> transposed = []
>>> for i in range (4):
	transposed.append([row[i] for row in matrix])

	
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
>>> 
