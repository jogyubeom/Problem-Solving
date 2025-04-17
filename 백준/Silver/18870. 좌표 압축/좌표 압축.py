import sys
input = sys.stdin.readline
    
N = int(input())
nodes = list(map(int, input().split()))
nodes2 = sorted(set(nodes))
dict = dict()
for i in range(len(nodes2)):
    dict[nodes2[i]] = i

for n in nodes:
    print(dict[n], end=' ')