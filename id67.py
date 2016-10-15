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
                flag = False
        i += 1
    return max(lst[-level:])

with open('p067_triangle.txt') as file:
    pyramid=file.read().split()
for i in range(len(pyramid)):
    pyramid[i] = int(pyramid[i])
print(findMax2(pyramid))