#1. Iterate the given array of numbers and print only those numbers which are divisible by 5.
arr=[12,15,60,87,55,85,90]
arr1=[]
for i in arr:
    if i%5==0:
        arr1.append(i)
print(arr1)

#2. Write a program to check whether the given character is vowel or consonant.
def check_vowel(char):
    if len(char)!=1:
        return "Enter a single character"
    char=char.lower()
    if char.isalpha():
        if char in 'aeiou':
            return f"{char} is a vowel"
        else:
            return f"{char} is a constant"
    else:
        return "Enter valid character"
char=input("enter a character:")
print(check_vowel(char))

#3.Write a program to count the occurence of even numbers and odd numbers between the range 10 – 55.
even_count = 0
odd_count = 0
for i in range(10,56):
    if i%2==0:
        even_count +=1
    else:
        odd_count +=1
print("Even numbers count:",even_count)
print("Odd numbers count:",odd_count)

#4. Write a program in Python to print numbers ranging from 1 to 25 but excluding numbers which are the multiples of 5.
for i in range(1,26):
    if i%5 !=0:
        print(i, end=" ")

#5. Write a program that takes an array of numbers and calculates the factorial of each element using a for loop, then prints the results
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
arr=[1,2,5,6,8]
for i in arr:
    print("The factorial of ",i, "is",factorial(i))

#6. Given two integer numbers return their product. If the product is greater than 500, then return their sum.
int1=int(input("Enter first integer:"))
int2=int(input("Enter second integer:"))
def calcint(a,b):
    product=a*b
    if product>500:
        return a+b
    else:
        return product
print(calcint(int1,int2))

#7. Write a program to print the greatest of two numbers.
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if num1>num2:
    print(f"{num1} is the greatest.")
elif num2>num1:
    print(f"{num2} is the greatest.")
else:
    print("Both are equal.")

#8. Write a program to print the greatest of three numbers.
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
if num1 >= num2 and num1 >= num3:
        print(f"{num1} is greatest")
elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is greatest")
else:
        print(f"{num3} is greatest")

#9. Write a program to separate positive and negative numbers from a list.
def separate(nums):
    positive_nums = []
    negative_nums = []
    for i in nums:
        if i >0:
            positive_nums.append(i)
        else:
            negative_nums.append(i)
    return "Positive numbers:",positive_nums,"Negative numbers:",negative_nums
nums = [23, 4, -6, 23, -9, 21, 3, -45, -8]
print(separate(nums))


