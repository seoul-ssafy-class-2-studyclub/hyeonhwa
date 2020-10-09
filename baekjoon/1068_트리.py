n = int(input())
parents = list(map(int, input().split()))
nodes = [[] for _ in range(n)]
delete_node = int(input())
for i in range(n):
    if i == delete_node:
        continue
    if parents[i] != -1:
        nodes[parents[i]].append(i)
queue = [delete_node]
for x in queue:
    for nd in nodes[x]:
        if nd not in queue:
            queue.append(nd)
nodes[delete_node] = [-1]
for x in queue:
    for node in nodes:
        if x in node:
            node.remove(x)
for x in queue:
    nodes[x] = -1
print(nodes.count([]))
# print(nodes)