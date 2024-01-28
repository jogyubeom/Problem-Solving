max_score = 0
for n in range(1,6):
    player = list(map(int,input().split()))
    if sum(player) > max_score:
        max_score = sum(player)
        winner = n

print(winner, max_score, sep=' ')
