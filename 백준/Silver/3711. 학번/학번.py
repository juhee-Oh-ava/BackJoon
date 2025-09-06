N = int(input())

for test_case in range(N):
    lst = []

    G = int(input())

    for _ in range(G):
        lst.append(int(input()))

    m = 1
    while True:
        result = set()

        for n in lst:
            result.add(n % m)
        if len(result) == G:
            break

        else:
            m += 1

    print(m)