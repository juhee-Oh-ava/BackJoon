N = input()
F = int(input())

start = int(N[:-2] + '00')
end = int(N[:-2] + '99')

target = 0

for i in range(start, end + 1):
    if i % F == 0:
        target = i
        break
        
print(str(target)[-2:])
        




