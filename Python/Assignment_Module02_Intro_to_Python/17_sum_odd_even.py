import math
n = int(input("Enter the number to stop = "))

def sum_of_odd(n):
    res = 0
    for i in range(1, n+1):
        if i % 2 != 0:  # odd number
            res+=(i**2)/ math.factorial(i)
    return res



print("Sum of Odd Series:", sum_of_odd(n))
