# 1. Program to identify if the  number is positive or negative
num=int(input("Enter a number:"))
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")



#2. Program to identify if the number is even or odd
#Method 1
def oddEven(num):
    if num%2==0:
        return "The number is even"
    else:
        return "The number is odd"
num=int(input("Enter a number:"))
print(oddEven(num))

#Method 2 :(using bitwise operator)
def isEven(num):
    return not num&1
num = int(input("Enter a number:"))
if isEven(num):
    print('The number is even')
else:
    print('The number is odd')


#3. Program to find Power of a number
def powerofnum(base,exp):
    return base ** exp
base=int(input('Enter base:'))
exp=int(input('Enter exponent:'))
result=powerofnum(base, exp)
print(f"{base} raised to the power {exp} is {result}")


#4. Write a program that takes two numbers as input and prints which one is greater (or if they are equal) using if-else statements.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")


#5.Write a program that takes a year as input and prints whether it's a leap year or not using if-else statements.
year=int(input("Year:"))
if (year%4==0 and year%100 !=0) or (year%400==0):
    print("Leap year")
else:
    print("Not a leap year")

#6. Write a program that takes a student's score as input and prints their grade (A, B, C, D, or F) using if-else statements
mark=float(input("Enter the mark:"))
if  mark >= 90:
    print("Grade A")
elif  mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C")
elif mark>=60:
    print("Grade D")
elif mark >=50:
    print("Grade E")
else:
    print("Grade F")

#7.Using if statements, else if , and else statements, make a program which displays a different message depending on the age given.
age=int(input("Enter age:"))
if age<16:
    print("You can't drive")
elif 16<= age <=17:
    print("You can drive but not vote.")
elif 18 <= age <=24:
    print("You can vote but not rent a car.")
else:
    print("You can do pretty much anything.")

#8.Write a program that prints the numbers from 1 to 100.For multiples of 3 print "Fizz",multiples of 5 print "Buzz" multiples of 3 and 5 print "FizzBuzz"
for num in range(1,101):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%3==0:
        print('Fizz')
    elif num%5==0 :
        print('Buzz')
    else:
        print(num)

#9.Leap year or not
def leapornot(year):
    if (year%4==0 and year%100 !=0) or year%400==0:
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
year=int(input("Enter the year="))
print(leapornot(year))