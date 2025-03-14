import random

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_str = ''
    for i in range(length):
        result_str += random.choice(letters)
    return result_str