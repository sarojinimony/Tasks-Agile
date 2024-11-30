#1. Write a program that prints numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#2. Write a program that prints even numbers from 1 to 20 using a for loop.
#Method 1
for i in range(1,21):
    if i%2==0:
        print(i)
#Method 2
for i in range(2,21,2):
    print(i)

#3. Write a program that prints odd numbers from 1 to 20 using a for loop.
#Method 1
for i in range(1,21):
    if i%2!=0:
        print(i)

#Method 2
for i in range(1,21,2):
    print(i)

#4. Write a program that calculates the factorial of a number using a for loop.
num=int(input('Enter a number:'))
factorial=1
for i in range(num,0,-1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")

#5.Write a program that calculates the sum of numbers from 1 to 100 using a for loop.
sum=0
for i in range(0,101):
    sum += i
print("The sum is",sum)

#6.Write a program that calculates the average of numbers in an array using a for loop.
arr=[10,20,30,40,50,60,70,80,90,100]
sum=0
for i in arr:
    sum += i
avg=sum/len(arr)
print("The average is :",avg)

#7. Write a program that uses nested for loops to draw patterns (e.g., squares, triangles, diamonds).
#square
n=5
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()

#triangle
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end=" ")
    print()

#diamond
n=5
for i in range(1,n+1):
    print(" " * (n-i),end=" ")
    print('*' * (2*i-1))
for i in range(n-1,0,-1):
    print(" " * (n-i),end=" ")
    print('*'*(2*i-1))

#8.Check if the first and last number of a list is the same
list=[10,20,30,40,10]
if list[0]==list[-1]:
    print("The result is true")
