n = int(input())
nodes = [-1]*(n+1)
nodes[1] = 0
queue = [1]
connected = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
while queue:
    x = queue.pop(0)
    arr = connected[x]
    for i in arr:
        if nodes[i] == -1:
            nodes[i] = x
            queue.append(i)
print('\n'.join(list(map(str, nodes[2:]))))
