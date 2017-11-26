"""
Write a higher order generalized mapping function that takes a list and
maps every element of that list into another list and return that list
"""


def my_map_func(seq, oprn):
    """
    higher order generalized mapping function
    """
    return [oprn(item) for item in seq]


def main():
    """
    running the code
    """
    print my_map_func(range(1, 11), lambda (x): x % 2 != 0)
    # will print
    # [True, False, True, False, True, False, True, False, True, False]

if __name__ == "__main__":
    main()
