A, B = input().split()
lengthA = len(A)
lengthB = len(B)
gap = lengthB - lengthA
plus = 0
result = 1e9
while True:
    count = 0
    for i in range(lengthA):
        if A[i] != B[i + plus]:
            count += 1
    result = min(result, count)
    if plus == gap:
        break
    plus += 1

print(result) 
