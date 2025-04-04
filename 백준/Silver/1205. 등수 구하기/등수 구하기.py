N, score, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
else:
    rankBoard = list(map(int, input().split()))
minScore = rankBoard[-1]

if N == P and score <= minScore :
    print(-1)

else:
    rank = 1
    for n in rankBoard:
        if n > score:
            rank += 1
    print(rank)
