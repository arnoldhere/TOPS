def sum_of_n_integers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Taking input from the user
n = int(input("Enter a positive integer: "))
if n > 0:
    result = sum_of_n_integers(n)
    print(f"The sum of the first {n} positive integers is: {result}")
else:
    print("Please enter a positive integer greater than 0.")