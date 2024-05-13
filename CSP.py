def valid_row(row, numbers):
    count = 0
    for i in range(len(row)):
        b = row[i]
        # print(b)
        if b == '1':
            count += 1

        if b == '0' or i == len(row)-1:
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
        if row[s-1] == 0:
            actions.append('L')
    if e+1 < len(row):
        if row[e+1] == 0:
            actions.append('R')
    return actions


def getPosition(row, numbers):
    result = []
    for i in range(len(row)):
        b = row[i]
        if b == '1':
            if row[i-1] != '1':
                s = i
            count += 1

        if b == '0' or i == len(row)-1:
            e = i
        result.append([s, e])


row = '0101'
numbers = [1, 1]
res = valid_row('0101', [1, 1])
print(res)
