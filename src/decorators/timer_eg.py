import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Δt = {end_time - start_time:.4f}")
        return result
    return wrapper


# @timer
def prime_factorization(n):
    start_time = time.time()
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    end_time = time.time()
    print(f"Δt = {end_time - start_time:.4f}")
    return factors


##########################################################
##### Test calls to the prime factorization function #####
integers = [2**20+1, 2**23+1, 2**29+1, 2**32+1]
for n in integers:
    result = prime_factorization(n)
    print(result)
##########################################################


#################################################################
##### Test the timer function without using syntactic sugar #####
# prime_factorization_timer = timer(prime_factorization)
# integers = [2**20+1, 2**23+1, 2**29+1, 2**32+1]
# for n in integers:
#     result = prime_factorization_timer(n)
#     print(result)
#################################################################


#######################################################
##### Test the prime factorization with decorator #####
# result = prime_factorization(2**29+1)
# print(result)
#######################################################