from collections import deque
def check(l):
    visit = [False]*(N+1)
    arr = l[:]
    queue = deque()
    queue.append(arr.pop(0))
    if arr == []:
        return True
    while queue:
        x = queue.pop()
        for i in near[x]:
            if not visit[i]:
                if i in arr:
                    arr.remove(i)
                    visit[i] = True
                    queue.append(i)
        if arr == []:
            return True
    return False


N = int(input())
people = list(map(int, input().split()))
near = [[] for _ in range(N+1)]
for i in range(1, N+1):
    l = list(map(int, input().split()))
    for j in l[1:]:
        near[i].append(j)
res = 987654321
for i in range(1<<N):
    vote1 = []
    vote2 = []
    for j in range(N):
        if i & (1 << j):
            vote1.append(j+1)
        else:
            vote2.append(j+1)
    if not vote1:
        continue
    if not vote2:
        continue
    if not check(vote1):
        continue
    if not check(vote2):
        continue
    p1, p2 = 0, 0
    for k in vote1:
        p1 += people[k-1]
    for k in vote2:
        p2 += people[k-1]
    res = min(res, abs(p1-p2))
if res == 987654321:
    res = -1
print(res)
