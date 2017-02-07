# -*- coding: UTF-8 -*-
# Use Python 2.x to run this script
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,

begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value

by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the

938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def string_score(string):
    string = string.lower()
    sum = 0
    for char in string:
        sum += ord(char) -96

    return sum


def method_cw():
    file = open('p022_names.txt', 'r')
    names = []
    names = file.read().split(',')

    for i in range(len(names)):
        names[i] = names[i][1:-1]
    names.sort()
    result = 0

    for i in range(len(names)):
        result += string_score(names[i]) * (i + 1)

    return result


if __name__ == '__main__':
    print method_cw()