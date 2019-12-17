from collections import deque

def tsort():
    fres = ''
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            fres += f'{i}'
    for _ in range(n):
        if len(queue) > 1:
            return '?'
        if not queue:
            return 'IMPOSSIBLE'
        x = queue.popleft()
        for i in neworder[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
                fres += f' {i}'
    return fres


res = []
for _ in range(int(input())):
    n = int(input())
    neworder = [[] for ___ in range(n+1)]
    indegree = [0] * (n+1)
    team = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            neworder[team[i]].append(team[j])
            indegree[team[j]] += 1
    for __ in range(int(input())):
        a, b = map(int, input().split())
        if b in neworder[a]:
            neworder[a].remove(b)
            neworder[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
        elif a in neworder[b]:
            neworder[b].remove(a)
            neworder[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1
    res.append(tsort())
print('\n'.join(res))
