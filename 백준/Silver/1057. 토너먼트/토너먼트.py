N, kim, lim = map(int, input().split())
roundNum = 0

while kim != lim:
    roundNum += 1
    kim -= kim // 2
    lim -= lim // 2

print(roundNum)