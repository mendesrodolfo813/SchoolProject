import math
def is_perfect_square(x):
    root = int(math.sqrt(x))
    return x == root * root

x = 25
if is_perfect_square(x):
    print("x is a perfect square.")
else:
    print("x is not a perfect square.")
