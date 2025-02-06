from functools import reduce


def find_prime_factor_add_to_list(number):
    prime_factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1

    print(prime_factors)
    result = reduce(lambda x, y: x*y, prime_factors)

    if result == number:
        print("Well Done!!")


find_prime_factor_add_to_list(630)
