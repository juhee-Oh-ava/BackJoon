T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_v = lst[0]
    min_v = lst[0]

    for i in range(N):
        if lst[i] > max_v:
            max_v = lst[i]

    for j in range(N):
        if lst[j] < min_v:
            min_v = lst[j]

    print(min_v, end=' ')
    print(max_v)




