def dfs(y, x):
    dx = [-1, 0, 1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, -1, 1, -1, 1]
    visited[y][x] = 1
    cr, cc = y, x

    for d in range(8):
        nr = cr + dy[d]
        nc = cc + dx[d]

        if nr < 0 or nr >= h or nc < 0 or nc >= w:
            continue
        if data[nr][nc] == 1 and not visited[nr][nc]:
            dfs(nr, nc)




while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for r in range(h):
        for c in range(w):
            if data[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                cnt += 1
    print(cnt)
