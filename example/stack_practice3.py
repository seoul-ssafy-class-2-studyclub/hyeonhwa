dfs = [False for i in range(7)]
road = [[1, 2], [1, 3], [2, 4], [2, 5], [4, 6], [5, 6], [6, 7], [3, 7]]
stack = []
check = '1'
if not stack:
    stack.append(1)
    dfs[0] = True
while stack:
    for j in road[:]:
        if stack[-1] == j[0] and dfs[j[1]-1] == False:
            stack.append(j[1])
            dfs[j[1]-1] = True
            check += ' {}'.format(j[1])
            road.remove(j)
        elif stack[-1] == j[1] and dfs[j[0]-1] == False:
            stack.append(j[0])
            dfs[j[0]-1] = True
            check += ' {}'.format(j[0])
            road.remove(j)
        elif stack[-1] in j and (dfs[j[0]-1] == True and dfs[j[1]-1] == True):
            stack.pop(-1)
    if False not in dfs:
        break
print(check)
