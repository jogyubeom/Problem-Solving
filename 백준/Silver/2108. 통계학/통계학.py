N = int(input())
numbers = []
numlst = [0] * 8001
maxnum = -4001
minnum = 4001
for _ in range(N):
    num = int(input())
    numbers.append(num)
    maxnum = max(maxnum, num)
    minnum = min(minnum, num)
    if num < 0:
        numlst[4000 - num] += 1
    else:
        numlst[num] += 1
numbers.sort()
print(round(sum(numbers) / N))
print(numbers[N//2])
mostnum = max(numlst)
mostlst = []
for i in range(8001):
    if numlst[i] == mostnum and i > 4000:
        mostlst.append(-(i - 4000))
    elif numlst[i] == mostnum and i <= 4000:
        mostlst.append(i)
if len(mostlst) == 1:
    print(mostlst[0])
else:
    mostlst.sort()
    print(mostlst[1])
print(maxnum - minnum)