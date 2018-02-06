def  palindrome(n,nreverse):
     if n==nreverse:
         print("Palindrome Number.")
     else:
         print("Not a Palindrome Number.")

n=input("Enter the number : ")
nreverse=n.reverse()
print(n)
print(nreverse)
palindrome(n,nreverse)
