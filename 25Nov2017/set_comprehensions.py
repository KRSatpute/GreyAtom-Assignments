"""
set comprehensions
"""


def generate_primes_less_than_n(num):
    """
    generate prime numbers less than num
    """
    return {x for x in range(2, num)
            if all(x % y for y in range(2, min(x, 11)))}


def get_ordered_prime_pairs(num):
    """
    generate a set of ordered pairs consisting of all of the prime pairs
    consisting of primes less than num
    """
    primes = generate_primes_less_than_n(num)
    return {(x, x + 2) for x in primes if x + 2 in primes} | {(2, 3), }


def main():
    """
    running the code
    """

    print generate_primes_less_than_n(100)
    print get_ordered_prime_pairs(100)

if __name__ == "__main__":
    main()
