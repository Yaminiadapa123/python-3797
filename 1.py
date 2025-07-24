n=int(input("enter a number :"))
t=n
x=0
while(n>0):
    r=n%10
    x=x*10+r
    n=n/10
if(t==x):
    print(" its a palindrome")
else:
    print("not a palindrome")