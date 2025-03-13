import random

def get_random_code(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(characters) for i in range(length))

print(get_random_code(10))