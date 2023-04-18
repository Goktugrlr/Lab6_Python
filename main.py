#Task 1
n = int(input("Please enter a value for n: "))
while True:
    x = int(input("Please enter a value for x: "))
    if x < 0:
        print("x must not be negative number. Try again!")
    else:
        break

factorial_results = lambda x: 1 if x == 0 else x * factorial_results(x-1)


result = [(n**i)/factorial_results(i) for i in range(x+1)]

sum_result = sum(result)

print(sum_result)



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
    n = int(input("Please enter a variable for summation as a constraint:"))
    if n < 1:
        print("Summation step is starting from 1. You should enter 1 or higher:")
    else:
        summation(n)
        break
