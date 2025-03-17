import random

def get_random_code(length):
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    return ''.join([random.choice(char_set) for _ in range(length)])