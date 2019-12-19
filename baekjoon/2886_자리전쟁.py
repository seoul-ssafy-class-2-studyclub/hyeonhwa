R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
people = []
chair = []
for x in range(R):
    for y in range(C):
        if board[x][y] == 'X':
            people.append((x, y))
        elif board[x][y] == 'L':
            chair.append((x, y))
if len(people) <= 1:
    print(0)
else:
    rc = [[] for _ in range(len(chair))]
    rp = [[] for _ in range(len(people))]
    for i in range(len(chair)):
        cx, cy = chair[i]
        for j in range(len(people)):
            px, py = people[j]
            rc[i].append(((px-cx)**2 + (py-cy)**2, j))
            rp[j].append(((px-cx)**2 + (py-cy)**2, i))
    res = [False]*(len(chair))
    result = 0
    for j in range(len(rp)):
        rp[j].sort(key=lambda x:x[0])
    for i in rc:
        l = sorted(i, key=lambda x:x[0])
        if rp[l[0][1]][0][0] == l[0][0]:
            res[rp[l[0][1]][0][1]] = True
            if l[0][0] == l[1][0]:
                result += 1
        else:
            flag = 0
            for j in range(1, len(rp)-1):
                for k in range(len(rc)):
                    if res[rp[l[j][1]][k][1]]:
                        continue
                    elif (not res[rp[l[j][1]][k][1]] and rp[l[j][1]][k][0] != l[j][0]):
                        break
                    elif flag == 0:
                        if rp[l[j][1]][k][0] == l[j][0]:
                            res[rp[l[j][1]][k][1]] = True
                            flag = 1
                            if l[j][0] == l[j+1][0]:
                                result += 1
                            break
                if flag == 1:
                    break
    print(result)