from collections import deque

def bfs(r, c, num):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    q = deque([(r, c)])

    while q:
        cr, cc = q.popleft()
        visited[cr][cc] = 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if data[nr][nc] > num:
                    q.append((nr, nc))
                    visited[nr][nc] = 1


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
li_M = []
li_m = []
result = 0

for row in data:
    M = max(row)
    li_M.append(M)
    m = min(row)
    li_m.append(m)

re_M = max(li_M)
re_m = min(li_m)


for i in range(re_M + 1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if data[r][c] > i and visited[r][c] == 0:
                cnt += 1
                visited[r][c] = 1
                bfs(r, c, i)
    result = max(cnt, result)
print(result)