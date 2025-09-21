from collections import deque

def bfs(r, c, alpha):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    q = deque([(r, c)])
    visited[r][c] = 1
    count = 1   # 영역 크기

    while q:
        cr, cc = q.popleft()

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < M and 0 <= nc < N and visited[nr][nc] == 0:
                if data[nr][nc] == alpha:
                    visited[nr][nc] = 1
                    count += 1
                    q.append((nr, nc))
    return count


N, M = map(int, input().split())
data = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

power_W = 0
power_B = 0

for r in range(M):
    for c in range(N):
        if visited[r][c] == 0:
            size = bfs(r, c, data[r][c])
            if data[r][c] == 'W':
                power_W += size ** 2
            else:  # 'B'
                power_B += size ** 2

print(power_W, power_B)
