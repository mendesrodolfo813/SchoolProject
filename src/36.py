def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("Enter the number of terms: "))
print(f"The Fibonacci sequence up to {n} terms is: {fibonacci(n)}")
