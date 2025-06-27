def fibonacci_series(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
result = fibonacci_series(n)
print("First few Fibonacci numbers\n", result )
