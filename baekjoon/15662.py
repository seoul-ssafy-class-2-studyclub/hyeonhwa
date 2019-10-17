def rotate(n, arr):
    if n == 1:
        arr.insert(0, arr.pop())
    else:
        arr.append(arr.pop(0))
    return arr


N = int(input())
gear = [[int(i) for i in input()] for _ in range(N)]
K = int(input())
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
    while y < N-1:
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
for i in range(N):
    if gear[i][0] == 1:
        score += 1
print(score)
