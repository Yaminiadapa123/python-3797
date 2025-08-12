# if else
'''
num=int(input("enter a number :"))
if num%2==0:
    print("even number")
else:
    print("odd number")
    
num = int(input("Enter a number: "))

if num == 0:
    print("zero")
else:
    if num>0:

        print("positive number")
    else:
        print("negative number")


age=int(input("enter your age:"))
if age>=18:
    print("you are eligible for vote")
else:
    print("you are not eligible for vote")
    
year=int(input("enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year : "))

a=int(input("enter first number :"))
b=int(input("enter second number :"))
if a==b:
    print("both are biggest numbers")
else:
    if a>b:

       print(f"a {a} is greater")
    else:
      print(f"b {b} is greater")
      '''
english_marks = int(input("Enter English marks: "))
maths_marks = int(input("Enter Maths marks: "))
telugu_marks = int(input("Enter Telugu marks: "))

total_marks = english_marks + maths_marks + telugu_marks
average = (total_marks / 300) * 100

print(f"Total marks are {total_marks}, Average is {average:.2f}%")

if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
elif average >= 50:
    print("Grade E")
else:
    print("Fail")
