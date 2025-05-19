import random
import math
from functools import reduce

def generate_random_sequence(n):
    """
    Generates a sequence of n randomly chosen numbers between 0 and 100.
    
    Args:
        n (int): Number of elements in the sequence.

    Returns:
        list: A list containing n randomly chosen integers between 0 and 100.
    """
    return [random.randint(0, 100) for _ in range(n)]

def calculate_average(sequence):
    """
    Calculates the average of a given sequence of numbers.
    
    Args:
        sequence (list): A list of numbers representing a sequence.

    Returns:
        float: The average of the sequence.
    """
    return reduce(lambda x, y: x + y / len(sequence), sequence, 0)

def check_random_sequences(sequence1, sequence2):
    """
    Checks if two sequences have the same elements in any order and calculates their averages.
    
    Args:
        sequence1 (list): The first sequence of numbers.
        sequence2 (list): The second sequence of numbers.

    Returns:
        tuple: A tuple containing a boolean indicating whether or not the sequences are the same,
              and two average values for comparison.
    """
    return (
        sequence1 == sequence2, 
        calculate_average(sequence1), 
        calculate_average(sequence2)
    )

def main():
    # Example 1
    n = 5
    random_sequence = generate_random_sequence(n)
    print(f"Random sequence: {random_sequence}")

    # Example 2
    random_sequence1 = generate_random_sequence(5)
    random_sequence2 = generate_random_sequence(3)

    average_a, avg_b = calculate_average(random_sequence), calculate_average(random_sequence1)
    if check_random_sequences([random_sequence], [random_sequence1]):
        print(f"Sequences are the same: {average_a == avg_b}")
    
    return

if __name__ == "__main__":
    main()
