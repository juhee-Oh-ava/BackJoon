A, B = map(int, input().split())
check = False
result = []
x1 = int(-A + ((A**2 - B)**0.5))
x2 = int(-A - ((A**2 - B)**0.5))
lst = [x1, x2]

if x1 % 1 == 0 and x2 % 1 == 0:
    result = sorted(lst)
    check = True
    # print(*result)
    if x1 == x2:
    # print(x1)
        check = False

if check:
    print(*result)
else:
    print(x1)


