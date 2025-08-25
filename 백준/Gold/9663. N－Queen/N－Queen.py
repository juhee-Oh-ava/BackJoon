def recur(row):
    global cnt
    if row == N:
        cnt += 1   # 모든 행에 퀸을 다 놓았을 때만 카운트
        return

    for col in range(N):
        if check1[col] == 0 and d1_check[row + col] == 0 and d2_check[row - col + N - 1] == 0:
            # 퀸 배치
            check1[col] = 1
            d1_check[row + col] = 1
            d2_check[row - col + N - 1] = 1

            recur(row + 1)  # 다음 행으로 진행

            # 백트래킹 (원상복구)
            check1[col] = 0
            d1_check[row + col] = 0
            d2_check[row - col + N - 1] = 0


N = int(input())
check1 = [0] * N
d1_check = [0] * (2 * N - 1)
d2_check = [0] * (2 * N - 1)
cnt = 0
recur(0)
print(cnt)