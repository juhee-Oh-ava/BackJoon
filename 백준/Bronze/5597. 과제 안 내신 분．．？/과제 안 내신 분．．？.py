students = [0]*31

for i in range(28):
    applied = int(input())
    students[applied] = 1

for i in range(1, len(students)):
    if students[i] != 1:
        print(i)

