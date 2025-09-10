def dfs(u):
    global cnt
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs(v)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False]*(N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)



