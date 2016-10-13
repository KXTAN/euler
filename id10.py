import math

"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def prime(n):
    prime_list = []
    bool_array = [True for x in range(n+1)]

    for x in range(2, int(math.ceil(math.sqrt(n)))):
        if bool_array[x]:
            for y in range(x*x, n+1, x):
                bool_array[y] = False

    for x in range(2, n+1):
        if bool_array[x]:
            prime_list.append(x)

    return prime_list

print(sum(prime(2000000)))
