def get_random_code(length):
    characters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += random.choice(characters)
    return result
