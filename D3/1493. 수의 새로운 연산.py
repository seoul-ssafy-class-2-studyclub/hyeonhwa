import sys
sys.stdin = open('1493.txt', 'r')

p, x, y, cnt = 1, 1, 1, 1
position = {}
while p <= 45000:
    if y == 1:
        position[p] = [x, y]
        x = 1
        y += cnt
        cnt += 1
    else:
        position[p] = [x, y]
        y -= 1
        x += 1
    p += 1

T = int(input())
for t in range(T):
    p, q = map(int, input().split())
    result = [0, 0]
    for key in position.keys():
        if key == p:
            result[0] = result[0] + position[key][0]
            result[1] = result[1] + position[key][1]
        if key == q:
            result[0] = result[0] + position[key][0]
            result[1] = result[1] + position[key][1]
        if key > p and key > q:
            break
    for key in position.keys():
        if position[key] == result:
            print('#{} {}'.format(t+1, key))
        if position[key][0] > result[0] and position[key][1] > result[1]:
            break
