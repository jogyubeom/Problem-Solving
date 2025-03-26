N = int(input())
result = 0
if N <= 99:
    result += N
elif N <= 110:
    result += 99
else:
    result += 99
    number = 111
    while True:
        number = str(number)
        diff = int(number[1]) - int(number[0])
        for i in range(2, len(number)):
            if int(number[i]) - int(number[i-1]) != diff:
                break
        else:
            result += 1
        number = int(number)
        if number == N:
            break
        number += 1

print(result)
