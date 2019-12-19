from collections import deque

def still():
    res = 0
    visit = [[0]*(w+2) for _ in range(h+2)]
    queue = deque()
    queue.append((0, 0))
    visit[0][0] = 1
    while queue:
        x, y = queue.pop()
        for dx, dy in idx:
            if 0 <= x+dx < h+2 and 0 <= y+dy < w+2:
                if building[x+dx][y+dy] == '.' and not visit[x+dx][y+dy]:
                    queue.append((x+dx, y+dy))
                    visit[x+dx][y+dy] = 1
                elif building[x+dx][y+dy] == '$' and not visit[x+dx][y+dy]:
                    res += 1
                    building[x+dx][y+dy] = '.'
                    queue.append((x+dx, y+dy))
                    visit[x+dx][y+dy] = 1
                if 'A' <= building[x+dx][y+dy] <= 'Z' and not visit[x+dx][y+dy]:
                    if building[x+dx][y+dy].lower() in key:
                        building[x+dx][y+dy] = '.'
                        queue.append((x+dx, y+dy))
                    else:
                        doors[ord(building[x+dx][y+dy])-ord('A')].append((x+dx, y+dy))
                elif 'a' <= building[x+dx][y+dy] <= 'z':
                    if building[x+dx][y+dy] not in key:
                        key.add(building[x+dx][y+dy])
                        queue.extend(doors[ord(building[x+dx][y+dy])-ord('a')])
                    building[x+dx][y+dy] = '.'
                    queue.append((x+dx, y+dy))
    return res


result = []
for tc in range(int(input())):
    h, w = map(int, input().split())
    building = [['.']*(w+2) for __ in range(h+2)]
    for i in range(1, h+1):
        building[i][1:w+1] = list(input())
    key = set(input())
    doors = [deque() for _ in range(26)]
    idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result.append(still())
print(f'\n'.join(list(map(str, result))))
