"""

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

def num_of_collatz_terms(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count

def m1():
    max_num_of_collatz_terms = 0
    collatz = 0
    for x in range(1, 1000000):
        num_of_terms = num_of_collatz_terms(x)
        if num_of_terms > max_num_of_collatz_terms:
            max_num_of_collatz_terms = num_of_terms
            collatz = x
    return(collatz)

def m2():
    collatzTerm_list = {}
    num_of_terms = 0
    for x in range(1, 1000000):
        count = 0
        currentlyCounting = x
        while x != 1:
            if collatzTerm_list.get(x) is None:
                if x % 2 == 0:
                    x = int(x/2)
                    count += 1
                else:
                    x = int(3*x + 1)
                    count += 1
            else:
                count += collatzTerm_list[x]
                break
        if collatzTerm_list.get(currentlyCounting) is None:
            collatzTerm_list[currentlyCounting] = count
        if count > num_of_terms:
            num_of_terms = count
    return num_of_terms - 1

print(m2())




