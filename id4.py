"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
largestProduct = 0
for x in range(100,999):
    for y in range(100, 999):
        product = x * y

        if str(product) == str(product)[::-1]:
            if product > largestProduct:
                largestProduct = product

print(largestProduct)