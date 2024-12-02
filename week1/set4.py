#1.Write a function that filters & returns negative numbers from a given array.
arr=[9,-2,6,-3,-4,5,-6]
def filter_neg(arr):
    return [i for i in arr if i<0]
print(filter_neg(arr))

#2.In a given array, remove all the odd numbers and replace that number with 0 
arr=[5, 10, 15, 20, 22, 23]
def replaceodd(arr):
    for i in range(len(arr)):
        if arr[i]%2!=0:
            arr[i]=0
    return arr
print(replaceodd(arr))

#3.Write a program that gets several integers from the user. Sum up all the  Integers they give you. Stop looping when they enter a 0. Display the tottal
def sum_int():
    total = 0
    while True:
        num = int(input("Enter an integer : "))
        if num == 0:
            break
        total += num
    print("The total sum is:", total)
sum_int()

#4.Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
def sum_current_previous():
    previous = 0  
    for current in range(1, 11):
        total = current + previous
        print(f"Current: {current}, Previous: {previous}, Sum: {total}")
        previous = current
sum_current_previous()

#5.Write a program to count the occurence of even numbers and odd numbers between the range 10 – 55.
def count_even_odd():
    even_count = 0
    odd_count = 0
    for num in range(10, 56):
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even numbers count:",even_count)
    print("Odd numbers count:", odd_count)
count_even_odd()
