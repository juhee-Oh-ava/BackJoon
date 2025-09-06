import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stats = [list(map(int, input().split())) for _ in range(N)]

min_sum = float('inf')

strength = [s[0] for s in stats]
dex = [s[1] for s in stats]
intell = [s[2] for s in stats]

for s in strength:
    for d in dex:
        for i in intell:
            count = 0
            for st in stats:
                if s >= st[0] and d >= st[1] and i >= st[2]:
                    count += 1

            if count >= K:
                min_sum = min(min_sum, s+d+i)

print(min_sum)