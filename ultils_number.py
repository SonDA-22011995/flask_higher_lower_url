import random


def generate_random_number() -> int:
    return random.randint(0, 9)

def is_valid_int_input(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False

def compare_numbers(user_number: int, target_number: int) -> int:
    if user_number > target_number:
        return 0
    if user_number < target_number:
        return -1
    return 1
