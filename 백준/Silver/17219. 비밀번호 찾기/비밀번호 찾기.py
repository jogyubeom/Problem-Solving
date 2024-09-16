import sys

N, M = map(int, input().split())
sites = dict()
for _ in range(N):
    site, pw = input().split()
    sites[site] = pw
for _ in range(M):
    print(sites[input()])
