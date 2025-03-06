import random

def get_random_code():
    code = "".join([str(random.randint(0, 9)) for i in range(16)])
    return code