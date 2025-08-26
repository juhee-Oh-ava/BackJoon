import sys
sys.setrecursionlimit(10**6)

def dfs(cur_idx):
    global team
    visited[cur_idx] = True
    cycle.append(cur_idx)
    nx_idx = lst[cur_idx]

    if visited[nx_idx]:
        if nx_idx in cycle:
            team += cycle[cycle.index(nx_idx):]
        return
    else:
        dfs(nx_idx)


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))

    lst = [0] + data
    visited = [0] * (n+1)
    team = []

    for idx in range(1, n+1):
        if not visited[idx]:
            cycle = []
            dfs(idx)

    print(n-len(team))
