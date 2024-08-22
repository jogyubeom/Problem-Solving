m, n = map(int, input().split())
result = ''
while m >= n:
    num = m % n
    m = m // n
    if num > 9:
        if num == 10:
            result = 'A' + result
        elif num == 11:
            result = 'B' + result
        elif num == 12:
            result = 'C' + result
        elif num == 13:
            result = 'D' + result
        elif num == 14:
            result = 'E' + result
        elif num == 15:
            result = 'F' + result
    else:
        result = str(num) + result

if m > 9:
    if m == 10:
        result = 'A' + result
    elif m == 11:
        result = 'B' + result
    elif m == 12:
        result = 'C' + result
    elif m == 13:
        result = 'D' + result
    elif m == 14:
        result = 'E' + result
    elif m == 15:
        result = 'F' + result
else:
    result = str(m) + result

print(result)
