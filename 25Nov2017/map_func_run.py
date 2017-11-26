"""
Write a higher order generalized mapping function that takes a list and
maps every element of that list into another list and return that list
ex:

i) Given a list get a new list which is squares of all the elemments of the
list

ii) Given a list get a list which has squares of all the even numbers and
cubes of all the odd numbers from the list

Running the map_func
"""

from map_func import my_map_func


def squared(num):
    """
    return square of number
    """
    return num ** 2


def square_even_cube_odd(num):
    """
    return square if num is even else return cube
    """
    return num ** 2 if num % 2 == 0 else num ** 3


def main():
    """
    running the code
    """
    seq_a = [5, 8, 10, 1, 2]
    seq_b = [9, 3, 6, 4, 7]

    print my_map_func(seq_a, squared)  # will print [25, 64, 100, 1, 4]
    print my_map_func(seq_b, squared)  # will print [81, 9, 36, 16, 49]
    print my_map_func(
        seq_a, square_even_cube_odd)  # will print [125, 64, 100, 1, 4]
    print my_map_func(
        seq_b, square_even_cube_odd)  # will print [729, 27, 36, 16, 343]

if __name__ == "__main__":
    main()
