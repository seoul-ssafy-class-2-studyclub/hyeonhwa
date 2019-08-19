for t in range(1):
    V, E = map(int, input().split())
    e = list(map(int, input().split()))
    e = [e[i:i+2] for i in range(0,len(e),2)]
    road = [False for i in range(V)]
    checklist = []
    for i in e:
        if not checklist:
            checklist.append(i)
        elif checklist[-1][0] == i[1]:
            checklist.pop(-1)
            checklist.append(i)
    e.remove(checklist[-1])
    checklist = checklist[0]
    for i in checklist:
        road[i-1] = True
    while True:
        for i in e:
            if checklist[-1] == i[0] and road[i[1]-1] == False:
                checklist.append(i[1])
                road[i[1]-1] = True
                for j in e:
                    if j != i and i[1] == j[1]:
                        checklist.remove(i[1])
                        road[i[1]-1] = False
                        break
            elif checklist[-1] != i[0] and road[i[1]-1] == False:
                if i[0] not in checklist:
                    checklist.append(i[0])
                    road[i[0]-1] = True
                checklist.append(i[1])
                road[i[1]-1] = True
                for j in e:
                    if j != i and i[1] == j[1] and i[0] == j[1] and road[j[1]-1] == False:
                        if checklist[-2] == i[0]:
                            checklist.remove(i[0])
                            road[i[0]-1] = False
                        checklist.remove(i[1])
                        road[i[1]-1] = False
                        break
        if False not in road:
            break

                

    print(checklist)
