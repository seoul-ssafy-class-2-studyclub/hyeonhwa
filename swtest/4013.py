def rotate(n, arr):
    if n == 1:
        arr.insert(0, arr.pop())
    else:
        arr.append(arr.pop(0))
    return arr

for t in range(int(input())):
    K = int(input())
    gear = [list(map(int, input().split())) for _ in range(4)]
    reverse = {1:-1, -1:1}
    for _ in range(K):
        n, d = map(int, input().split())
        x, y = n-1, n-1
        rx, ry = d, d
        rot = [(n-1, d)]
        while x > 0:
            if gear[x-1][2] != gear[x][6]:
                rx = reverse[rx]
                rot.append((x-1, rx))
            else:
                break
            x -= 1
        while y < 3:
            if gear[y][2] != gear[y+1][6]:
                ry = reverse[ry]
                rot.append((y+1, ry))
            else:
                break
            y += 1
        for num, direction in rot:
            gear[num] = rotate(direction, gear[num])
        # print(gear)
    score = 0
    for i in range(4):
        if gear[i][0] == 0:
            score += 0
        else:
            if i == 0:
                score += 1
            elif i == 1:
                score += 2
            elif i == 2:
                score += 4
            else:
                score += 8
    print(f'#{t+1} {score}')
