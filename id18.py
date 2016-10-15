"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def findMax(lst):
    #greedy approach does not work
    maxSum = 0
    index = 0
    i = 1
    while True:
        print(maxSum, lst[index])
        maxSum += lst[index]

        if index+i >= len(lst):
            return maxSum
        elif lst[index+i] > lst[index+i+1]:
            index += i
        else:
            index += i+1
        i += 1

def findMax2(lst):
    #boundary conditions
    leftSlopeSum, rightSlopeSum = lst[0], lst[0]
    leftSlopeIndex = 0
    rightSlopeIndex = 0
    indicesOfSlopes = [0]
    counter = 1
    while rightSlopeIndex+counter+1 < len(lst):
        leftSlopeIndex += counter
        rightSlopeIndex += counter+1
        indicesOfSlopes.append(leftSlopeIndex)
        indicesOfSlopes.append(rightSlopeIndex)
        leftSlopeSum += lst[leftSlopeIndex]
        rightSlopeSum += lst[rightSlopeIndex]
        lst[rightSlopeIndex],lst[leftSlopeIndex] = rightSlopeSum, leftSlopeSum
        counter+=1
    #middle conditions
    i = 4
    level = 2
    flag = False
    while i < len(lst):
        if i not in indicesOfSlopes:
            lst[i] += max(lst[i-level], lst[i-level-1])
            flag = True
        else:
            if flag == True:
                level += 1
        i += 1
    return lst

with open('id18numbers') as file:
    pyramid=file.read().split()
for i in range(len(pyramid)):
    pyramid[i] = int(pyramid[i])
print(findMax2([3,7,4,2,4,6,8,5,9,3,1,2,3,4,5]))




