def findancestor(node):
    if node//2 >= 1:
        if not node%2 and N == node:
            tree[node//2] = tree[node]
        elif node%2:
            tree[node//2] = tree[node]+tree[node-1]
        findancestor(node-1)


T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    findancestor(N)
    print('#{} {}'.format(t+1, tree[L]))
