import sys
input = lambda: sys.stdin.readline().rstrip()

res = []
for _ in range(int(input())):
    n = int(input())
    students = list(map(int, input().split()))
    team = [0]*n
    group = 1
    for i in range(n):
        if team[i] == 0:
            while team[i] == 0:
                team[i] = group
                i = students[i]-1
            while team[i] == group:
                team[i] = -1
                i = students[i]-1
            group += 1
    res.append(str(n-team.count(-1)))
print('\n'.join(res))
        