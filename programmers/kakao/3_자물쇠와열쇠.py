def solution(key, lock):
    keys = []
    locks = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                locks.append((i, j))
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                keys.append((i, j))
    rules = []
    x, y = locks[0]
    for i in range(1, len(locks)):
        rx, ry = locks[i]
        dx = rx - x
        dy = ry - y
        rules.append((rx - x, ry - y))
        # rules[1].append((dy, -dx))
        # rules[2].append((-dy, dx))
        # rules[3].append((-dx, -dy))
    for i in range(len(keys)):
        visit = [0]*(len(rules))
        cnt = 0
        kx, ky = keys[i]
        for j in range(len(keys)):
            if i != j:
                kxx, kyy = keys[j]
                dx, dy = kxx - kx, kyy - ky
                for k in range(len(locks)-1):
                    if (dx, dy) == rules[k] and visit[k] == 0:
                        visit[k] = 1
                        cnt += 1
                if len(locks)-1 in cnt:
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))