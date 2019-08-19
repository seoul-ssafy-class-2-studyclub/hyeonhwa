T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    nodes = []
    for e in range(E):
        nodes += [list(map(int,input().split()))]
    check = list(map(int, input().split()))
    checklist = []
    for node in nodes:
        if check[0] == node[0]:
            checklist += [node]
    for i in checklist:
        for node in nodes:
            if i[1] == node[0]:
                checklist.append([i[0], node[1]])
    if check in checklist:
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))
