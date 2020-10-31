n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    nodes[b].append(a)
flag = 0
ans = []
for i in range(1, n+1):
    visit = [0]*(n+1)
    queue = [i]
    res = 1
    while queue:
        x = queue.pop()
        if visit[x] == 0:
            res += 1
            visit[x] = 1
            queue.extend(nodes[x])
    if flag < res:
        ans = [i]
        flag = res
    elif flag == res:
        ans.append(i)
print(' '.join(list(map(str, ans))))
