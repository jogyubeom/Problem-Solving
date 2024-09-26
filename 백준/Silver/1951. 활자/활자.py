
N = int(input())
count = N
gear = 1
while True:
    if N >= 10**gear:
        count += (N - (10**gear - 1))
    else:
        break
    gear += 1
print(count % 1234567)
