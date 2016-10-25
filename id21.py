
def sumfactorsOf(k):
    lst = []
    i = 1
    while i*i <= k:
        if k%i==0 and (i not in lst):
            lst.append(i)
            if i != k/i and i != 1:
                lst.append(int(k/i))
        i += 1
    return sum(lst)


def sumofAmicable(n):
    lstOfSums = []
    for i in range(0, n):
        lstOfSums.append(sumfactorsOf(i))
    visited = []
    sum = 0
    i = 0
    length = len(lstOfSums)
    while i < len(lstOfSums):
        if lstOfSums[i] < length and i not in visited:
            if lstOfSums[lstOfSums[i]] < length:
                if i == lstOfSums[lstOfSums[i]]:
                    visited.append(i)
                    visited.append(lstOfSums[i])
                    print(i, lstOfSums[i])
                    if i == lstOfSums[i]:
                        sum += i
                    else:
                        sum += i + lstOfSums[i]
        i += 1
    return sum

#check and see, answer still incorrect\
print(sumofAmicable(10000))