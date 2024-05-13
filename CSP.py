

def valid_Column(column, numbers):
    count = 0
    for i in range(len(column)):
        b = column[i]
        # print(b)
        if b == '1':
            count += 1

        if b == '0' or i == len(column)-1:
            if count in numbers:
                numbers.remove(count)
                count = 0
    if len(numbers) == 0:
        return True
    return False


def getActions(row, n):
    s, e = n

    actions = []
    if s-1 >= 0:
        if row[s-1] == '0':

            actions.append('L')

    if e+1 < len(row):
        if row[e+1] == '0':
            actions.append('R')
    return actions


def getPosition(row, numbers):
    result = []

    s = -1
    e = -1
    i = 0
    while i < len(row):
        b = row[i]
        if b == '1':
            s = i
            i = numbers[0] + i
            e = i - 1
            numbers.remove(numbers[0])
            result.append([s, e])
        i += 1
    return result


row = '011101'
numbers = [3, 1]

result = getPosition(row, numbers)
print(result)
