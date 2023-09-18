import random

def generate_random_number(range1, range2):
    """
    Generate a random number within the specified range [range1, range2].
    """
    return random.randint(range1, range2)

def test_if_int(map_tile):
    """
    Check if a given value can be converted to an integer.
    """
    try:
        int(map_tile)
        return True
    except ValueError:
        return False
