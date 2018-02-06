#Print a Fibonacci series up to n.
def fib(n):    
     a, b = 0, 1
     while a < n:
         print(a)
         a,b =b,a+b
         #print()
n=int(input("Enter the number : "))
fib(n)
