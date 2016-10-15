def number_to_letter(number):
    number_str = ''
    if number == 1000:
        return 'onethousand'

    if number == 0:
        return 'zero'

    if number < 1000:
        hundred = int(number / 100)

        if hundred == 1:
            number_str = number_str + 'one' + 'hundred'

        elif hundred == 2:
            number_str = number_str + 'two' + 'hundred'

        elif hundred == 3:
            number_str = number_str + 'three' + 'hundred'

        elif hundred == 4:
            number_str = number_str + 'four' + 'hundred'

        elif hundred == 5:
            number_str = number_str + 'five' + 'hundred'

        elif hundred == 6:
            number_str = number_str + 'six' + 'hundred'

        elif hundred == 7:
            number_str = number_str + 'seven' + 'hundred'

        elif hundred == 8:
            number_str = number_str + 'eight' + 'hundred'

        elif hundred == 9:
            number_str = number_str + 'nine' + 'hundred'
    tenth_number = number % 100
    if number > 100 and tenth_number != 0:
        number_str = number_str + 'and'

    if 10 < tenth_number < 20:
        if tenth_number == 11:
            number_str = number_str + 'eleven'
            return number_str

        elif tenth_number == 12:
            number_str = number_str + 'twelve'
            return number_str

        elif tenth_number == 13:
            number_str = number_str + 'thirteen'
            return number_str

        elif tenth_number == 14:
            number_str = number_str + 'fourteen'
            return number_str

        elif tenth_number == 15:
            number_str = number_str + 'fifteen'
            return number_str

        elif tenth_number == 16:
            number_str = number_str + 'sixteen'
            return number_str

        elif tenth_number == 17:
            number_str = number_str + 'seventeen'
            return number_str

        elif tenth_number == 18:
            number_str = number_str + 'eighteen'
            return number_str

        elif tenth_number == 19:
            number_str = number_str + 'nineteen'
            return number_str

    if tenth_number < 11 or tenth_number > 19:
        tenth_digit = int(tenth_number/10)

        if tenth_digit == 1:
            number_str = number_str + 'ten'

        elif tenth_digit == 2:
            number_str = number_str + 'twenty'

        elif tenth_digit == 3:
            number_str = number_str + 'thirty'

        elif tenth_digit == 4:
            number_str = number_str + 'forty'

        elif tenth_digit == 5:
            number_str = number_str + 'fifty'

        elif tenth_digit == 6:
            number_str = number_str + 'sixty'

        elif tenth_digit == 7:
            number_str = number_str + 'seventy'

        elif tenth_digit == 8:
            number_str = number_str + 'eighty'

        elif tenth_digit == 9:
            number_str = number_str + 'ninety'

    oneth_number = number % 10

    if oneth_number > 0:

        if oneth_number == 1:
            number_str = number_str + 'one'

        elif oneth_number == 2:
            number_str = number_str + 'two'

        elif oneth_number == 3:

            number_str = number_str + 'three'

        elif oneth_number == 4:
            number_str = number_str + 'four'

        elif oneth_number == 5:
            number_str = number_str + 'five'

        elif oneth_number == 6:
            number_str = number_str + 'six'

        elif oneth_number == 7:
            number_str = number_str + 'seven'

        elif oneth_number == 8:
            number_str = number_str + 'eight'

        elif oneth_number == 9:
            number_str = number_str + 'nine'

    return number_str

num_list = [x for x in range(1, 1001)]
letter_list = []

for x in num_list:
    letter_list.append(number_to_letter(x))

num_of_characters = 0
for letter in letter_list:
    print(letter)
    num_of_characters += len(list(letter))

print(num_of_characters)