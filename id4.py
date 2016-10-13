"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def palindromeCheck(digit):
    string = str(digit)
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

def m1():
    largestProduct = 0
    for x in range(100,999):
        for y in range(100, 999):
            product = x * y
            if palindromeCheck(product) and product>largestProduct:
                largestProduct = product
    return(largestProduct)

print(m1())

