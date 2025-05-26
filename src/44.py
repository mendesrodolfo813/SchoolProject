def fibonacci_sequence(n):
    """
    Generate a list of Fibonacci numbers up to n.
    
    Parameters:
    n (int): The upper limit of the Fibonacci sequence generation.
    
    Returns:
    list: A list containing the first 'n' Fibonacci numbers.
    """
    if n <= 1:
        return [0, 1]
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

# Example usage:
n = 10
print(f"Fibonacci sequence up to {n}: ", fibonacci_sequence(n))
