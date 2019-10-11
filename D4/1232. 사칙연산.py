def calculator(a, b, c):
    if c == '-':
        return a-b
    elif c == '+':
        return a+b
    elif c == '*':
        return a*b
    else:
        return a/b


def retree(idx):
    queue = nodes[idx]
    while queue:
        x = queue.pop()
        if nodes[x]:
            if (type(tree[nodes[x][0]]) == int or type(tree[nodes[x][0]]) == float or tree[nodes[x][0]].isdigit()) and (type(tree[nodes[x][1]]) == int or type(tree[nodes[x][1]]) == float or tree[nodes[x][1]].isdigit()):
                tree[x] = calculator(int(tree[nodes[x][0]]), int(tree[nodes[x][1]]), tree[x])
            else:
                queue.append(x)
                queue.extend(nodes[x])
    

for t in range(10):
    N = int(input())
    treeinfo = [list(input().split()) for _ in range(N)]
    nodes = [[] for _ in range(N+1)]
    tree = [0] * (N+1)
    for i in treeinfo:
        if len(i) > 2:
            nodes[int(i[0])] += [int(i[2]), int(i[3])]
        tree[int(i[0])] = i[1]
    idx = 0
    retree(1)
    # print(tree)
    res = calculator(int(tree[2]), int(tree[3]), tree[1])
    print('#{} {}'.format(t+1, int(res)))
    