"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
def isPrime(k, listofPrimes):
    for i in range(1, len(listofPrimes)):
        if k%listofPrimes[i]==0:
            return False
    return True

def prime(n):
    primes = [2, 3]
    while len(primes)<n:
        nxt = primes[len(primes)-1]
        while not isPrime(nxt, primes):
            nxt+=2
        primes.append(nxt)
    return primes

primes = prime(10001)
print(primes[len(primes)-1])
#slow