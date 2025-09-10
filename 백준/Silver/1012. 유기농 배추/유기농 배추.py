def dfs(y, x):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited[y][x] = 1
    cr, cc = y, x
    for d in range(4):
        nr = cr + dy[d]
        nc = cc + dx[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if data[nr][nc] == 1 and not visited[nr][nc]:
            dfs(nr, nc)

T = int(input())

for test_case in range(T):
    M, N, K = map(int, input().split())
    data = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        data[y][x] =1

    for r in range(N):
        for c in range(M):
            if data[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                cnt += 1

    print(cnt)



