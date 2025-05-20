def add(a: int, b: int) -> int:
    """
    Adds two integers.
    
    Parameters:
        a (int): The first integer.
        b (int): The second integer.
        
    Returns:
        int: The sum of the two integers.
    """
    return a + b

def multiply(x: int, y: int) -> int:
    """
    Multiplies two integers.
    
    Parameters:
        x (int): The first integer.
        y (int): The second integer.
        
    Returns:
        int: The product of the two integers.
    """
    return x * y

def find_min_value(nums: list[int]) -> int:
    """
    Finds the minimum value in a list of integers.
    
    Parameters:
        nums (list[int]): A list of integers.
        
    Returns:
        int: The minimum value found in the list.
    """
    if not nums:
        return None
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

def check_function(func_name: str, *args) -> bool:
    """
    Checks whether a function returns the expected result.
    
    Parameters:
        func_name (str): The name of the function to be checked.
        *args: Arguments for the function to be tested.
        
    Returns:
        bool: True if the function's return value matches the expected result, False otherwise.
    """
    actual_result = func_name(*args)
    expected_result = 100
    return actual_result == expected_result

# Example usage:
if __name__ == "__main__":
    print(add(5, 3))  # Expected output: 8
    print(multiply(4, 7))  # Expected output: 28
    print(find_min_value([1, -3, 2, 5]))  # Expected output: -3
    print(check_function("add", 5, 3))  # Expected output: True
    print(check_function("multiply", 4, 7))  # Expected output: False
