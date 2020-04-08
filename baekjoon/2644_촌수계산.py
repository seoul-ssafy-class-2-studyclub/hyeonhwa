import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
people = [[] for _ in range(n+1)]

start, end = map(int, input().split())

for _ in range(int(input())):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

queue = [(0, start)]
visit = [0]*(n+1)

res = -1
for cnt, x in queue:
    for person in people[x]:
        if visit[person]:
            continue
        if person == end:
            res = cnt + 1
            break
        visit[person] = 1
        queue.append((cnt+1, person))
    if res != -1:
        break
print(res)