number = 2**1000
digits = list(str(number))
number_sum = 0
for digit in digits:
    number_sum += int(digit)

print(number_sum)