vyr = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def summa(vyr, sum=0):
    for i in range(len(vyr)):
        if type(vyr[i]) == int:
            sum = sum + vyr[i]
        else:
            sum = summa(vyr[i], sum)
    return (sum)


print(summa(vyr))
