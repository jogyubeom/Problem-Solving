A, B = input().split()
Aa = []
Bb = []
a = []
b = []
for i in range(len(A)):
    if A[i] == '5':
        Aa.append('6')
        a.append('5')
    elif A[i] == '6':
        Aa.append('6')
        a.append('5')
    else:
        Aa.append(A[i])
        a.append(A[i])

for i in range(len(B)):
    if B[i] == '5':
        Bb.append('6')
        b.append('5')
    elif B[i] == '6':
        Bb.append('6')
        b.append('5')
    else:
        Bb.append(B[i])
        b.append(B[i])

numa = int(''.join(a))
numb = int(''.join(b))
numA = int(''.join(Aa))
numB = int(''.join(Bb))

print(numa + numb, end=' ')
print(numA + numB)


