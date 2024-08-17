
n = int(input())
if n == 1 or n == 3:
    print(-1)
elif (n % 5) % 2 != 0:
    count1 = (n // 5) - 1
    count2 = ((n % 5) + 5) // 2
    print(count1 + count2)
else:
    count1 = n // 5
    count2 = (n % 5) // 2
    print(count2 + count1)