def recur(start, sum_v):
    global cnt
    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            sum_v += arr[i]

            if sum_v == S:
                cnt += 1

            recur(i + 1, sum_v)  # 다음 원소 탐색

            sum_v -= arr[i]      # 백트래킹
            visited[i] = 0

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
cnt = 0

recur(0, 0)
print(cnt)