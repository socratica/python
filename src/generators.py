# TITLE:  Generators in Python
# URL: https://www.youtube.com/watch?v=gMompY5MyPg

# >>>>>>>>>> The difference between 'return' and 'yield'
def f():
    return 1
    return 2
    return 3

# print(f())

def g():
    yield 1
    yield 2
    yield 3

# print(g())

# for y in g():
#     print(y)


# >>>>>>>>>> Create a generator of the lower-case English letters
import string
def letters():
    for c in string.ascii_lowercase:
        yield c

# for letter in letters():
#     print(letter)


# >>>>>>>>>> Create a generate that 'generates' the prime numbers
import itertools

def prime_numbers():
    # Handle the first prime
    yield 2
    prime_cache = [2]  # Cache of primes

    # Loop over positive, odd integers
    for n in itertools.count(3, 2):
        is_prime = True
        
        # Check to see if any prime number divides n
        for p in prime_cache:
            if n % p == 0:  # p divides n evenly
                is_prime = False
                break

        # Is it prime?
        if is_prime:
            prime_cache.append(n)
            yield n

# for p in prime_numbers():
#     print(p)
#     if p > 100:
#         break


# >>>>>>>>>> Loop over the generator of the squares
import itertools

squares = (x**2 for x in itertools.count(1))

# for x in squares:
#     print(x)
#     if x > 500:
#         squares.close()


# >>>>>>>>>> Check the type of the generator
import itertools

squares = (x**2 for x in itertools.count(1))

# print(type(squares))


# >>>>>>>>>> Check the size of a generator
import itertools
import sys

squares = (x**2 for x in itertools.count(1))

# print(sys.getsizeof(squares))