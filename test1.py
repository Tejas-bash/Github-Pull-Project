def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calculate the Fibonacci sequence for a large number
n = 35
print("Calculating Fibonacci sequence for n =", n)
result = fibonacci(n)
print("Fibonacci result for n =", n, ":", result)
