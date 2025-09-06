# import sys
# input = sys.stdin.readline

T = int(input())

for _ in range(T):
    lst = list(input().strip())   # 줄 끝 공백 제거
    N = int(len(lst)**0.5)
    arr = []

    for i in range(0, len(lst), N):
        arr.append(lst[i:i+N])

    rotated = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotated[r][c] = arr[c][N-1-r]

    result = ""
    for row in rotated:
        result += "".join(row)

    print(result)




