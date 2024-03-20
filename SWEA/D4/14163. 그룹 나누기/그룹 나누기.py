def make_set(n):
    return [i for i in range(n+1)]


def find_set(x):
    if parents[x] == x:
        return x

    return find_set(parents[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())    # 학생 수, 신청서 수
    apply = list(map(int, input().split()))     # 신청 내역
    parents = make_set(N)   # 각 학생(인덱스)의 소속 조
    for i in range(M):
        union(apply[2*i], apply[2*i + 1])
    for i in range(N+1):
        parents[i] = find_set(parents[i])
    parents = set(parents)
    print(f'#{tc} {len(parents)-1}')