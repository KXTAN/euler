"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#sort of brute force, sure have better ways
def prime_factors(n):
    """
    i will always be a prime if it goes into the else body.

    n is divided from 2 onwards, if its even it will be solved by the first case, else if n is odd,
    i will be a prime itself, or multiple of odds (which again will be cancelled out by some k < i, k is odd),
    therefore i must be prime.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

factors = prime_factors(600851475143)
print(factors[len(factors)-1])