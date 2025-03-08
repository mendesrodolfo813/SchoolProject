import random

def random_code(length=8):
    letters = "qwertyuiopasdfghjklzxcvbnm"
    numbers = "1234567890"
    special_characters = "#@!$%^&*()_+-=[]{}|;':\"<>,./?"
    code = ""
    for i in range(length):
        if i % 2 == 0:
            code += random.choice(letters)
        elif i % 3 == 0:
            code += random.choice(numbers)
        else:
            code += random.choice(special_characters)
    return code
