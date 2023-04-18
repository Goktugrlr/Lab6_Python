import math

#Task 1
n = int(input("Please enter a value for n: "))
while True:
    x = int(input("Please enter a value for x: "))
    if x < 0:
        print("x must not be negative number. Try again!")   #If x is negative,we can not apply that formula
    else:
        break

formula = lambda i: (n ** i) / math.factorial(i)

resultList = [formula(i) for i in range(x + 1)]

result = sum(resultList)

print(result)


#Task 2
result = 0
k = 1


def summation(n):
    global result
    global k
    if k <= n:                      #k should not exceed n
        result += (-1)**(k+1)/k     #add result according to given formula
        k += 1                      #increment base step
        summation(n)                #enter the recursive
    else:
        print(result)


while True:
    constraint = int(input("Please enter a variable for summation as a constraint:"))
    if constraint < 1:
        print("Summation step is starting from 1. You should enter 1 or higher:")
    else:
        summation(constraint)
        break
