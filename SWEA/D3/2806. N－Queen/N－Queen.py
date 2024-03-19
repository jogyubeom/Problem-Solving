def dfs(level):
    global count
    if level == N:
        count += 1
        return
    for j in range(N):
        if visited_c[j] != 0 or visited_rc[level+j] != 0 or visited_cr[level-j+N-1] != 0:
            continue
        visited_c[j] = 1
        visited_rc[level+j] = 1
        visited_cr[level-j+N-1] = 1
        dfs(level + 1)
        visited_c[j] = 0
        visited_rc[level+j] = 0
        visited_cr[level-j+N-1] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())    # N*N 보드, N개의 퀸
    count = 0
    visited_c = [0] * N
    visited_rc = [0] * (2*N-1)
    visited_cr = [0] * (2*N-1)
    dfs(0)
    print(f'#{tc} {count}')