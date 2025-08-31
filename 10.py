#looping 
# while loop
"""
n=1
while n<=100:
    print(n)
    n=n+1
    
n=100
while n>=0:
    print(n)
    n=n-1
    
n = 1
s = 0
while n <= 100:
    s = s + n
    n = n + 1
print(s)
"""  

#even numbers from 1 to 20
"""
n = 1
while n <= 20:
    r = n % 2
    if r == 0:
        print("Even number:", n)
    n = n + 1
"""

#Find the sum of numbers from 1 to n (where n is given by the user).
"""
n=int(input("enter a number  :"))
x=1
s=0
while x<=n:
    s=s+x
    x=x+1
    print("Sum from 1 to", n, "is", s)   
    
    """
#Print the multiplication table of a number entered by the user.
"""
n=int(input("enter a number  :"))
y=1
while y<=20:
    print(n,"*",y,"=",n*y)
    y=y+1
    """
#Reverse the digits of a given number
"""
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10
print("Reversed number is", rev)

  """    
#Check if a given number is a palindrome (same forwards and backwards).
"""  
n=int(input("enter a number :"))
x=0
t=n
while n>0:
    r=n%10
    x=x*10+r
    n=n//10
if t==x:
    print("its a palindrome")
else:
    print("not a palindrome")
    """  

#Keep asking the user to enter a number until they enter 0, then print the sum of all numbers entered.
""" 
n=int(input("enter a number :"))
s=0
num=n
while n>0:
    r=n%10
    s=s+r
    n=n//10
print("the sum of numbers ",num,"is",s)
    
""" 
#Find the factorial of a given number using a while loop.
""" 
n=int(input("enter a num :"))
num=n
f=1
while n>1:
    f=f*n
    n=n-1
print("the factorial of",num, "is",f)
""" 
#Find the sum of digits of a number until the result is a single digit.
""" 
n = int(input("Enter any number: "))
num = n

while n > 9:  
    s = 0
    while n > 0:
        r = n % 10
        s = s + r
        n = n // 10
    n = s  

print("Single digit of", num, "is", n)
""" 

#for loop
"""
text="yamini"
for i in text:
    print(i)

#2 numbers
num=6
for i in range(num):
    print(i)

#3 lists
hero=["pawankalyan","chiranjeevi","ramcharan"]
for y in hero:
    print(y)

"""
#printing numbers from 1 to 10
"""
n=10
for i in range(1,n+1): #range(start,stop)
    print(i)  
    """  

#Print all even numbers between 1 and 20.
"""
n=20
for m in range(2,n+1,2):
    print(m)
    """
##Print all odd numbers between 1 and 20.
"""
n=20
for a in range(1,n+1,2):
    print(a)

  """
 
#Print the multiplication table of a number (e.g., 5).
 
"""
n=int(input("enter a number :"))


for y in range(1,21) :

    print(n,"*",y,"=",n*y)


"""
#Print the squares of numbers from 1 to 10.
"""
n=1
for m in range(1,11):
     print("Square of", m, "is", m*m)
     """
#Print the reverse numbers from 10 to 1.
"""
for j in range(10,0,-1):
    print(j)
     """
#Print the sum of numbers from 1 to 100.
"""
s=0
for m in range(1,101):
    s=s+m
print("the sum of numbers from 1 to 100 :",s)

"""
#Print the factorial of a given number.
"""
num=int(input("enter a number:"))
f=1
for l in range(num,0,-1):
    f=f*l
    
print("factorial of given is ",f)
"""
# reverse a string
"""
name=input("enter a string :")
reverse_string=""
for char in name:
    reverse_string=char+reverse_string
print(reverse_string)
    
"""
#Write a program to check if a number is prime using a for loop.
"""
n=int(input("enter a number :"))
fc=0
for a in range(1,n+1):
    r=n%a
    if r==0:
        fc=fc+1
if fc==2:
    print("prime number")
else:
    print("not a prime number")
"""
# nested loop
"""
for i in range(5):
    for j in range(5):
        print(i,j)
"""
#2 
"""
for i in range(5):
    print("*")
"""
#3
"""
n=5
print("*"*n)
"""
#4
"""
n=5
for i in range(n):
    print("*",end="")
"""
#5
"""
n = 5
for i in range(n):          
    for j in range(n):       
        print("*", end=" ")   
    print()  
"""  
#6
for i in range(5):
    for j in range(5):
        print("#",end="" )
    print()
#7 increasing triangle pattern
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()            
