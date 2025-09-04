N = int(input())
cnt = 0

for i in range(2, N-1, 2):
    cnt += (N-i-2)//2

print(cnt)

