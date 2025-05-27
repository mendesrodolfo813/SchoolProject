def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def square_root(num: float) -> float:
    """
    Calculates the square root of a number.
    
    Args:
        num (float): The number to calculate the square root of.
        
    Returns:
        float: The square root of the given number.
    """
    if num < 0:
        raise ValueError("Cannot compute square root of negative numbers.")
    return num ** 0.5

def greet(name: str) -> None:
    """
    Prints a greeting message to the console.
    
    Args:
        name (str): The name to greet.
        
    Returns:
        None
    """
    print(f"Hello, {name}!")

# Example usage
if __name__ == "__main__":
    # Add two numbers
    result = add_numbers(5, 3)
    print(result)

    # Square root of the number
    sqrt_result = square_root(16.25)
    print(sqrt_result)

    # Print a greeting message
    greet("Alice")
