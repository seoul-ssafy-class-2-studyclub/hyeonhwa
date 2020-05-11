import sys
input = lambda: sys.stdin.readline().rstrip()

def color_blind():
    visit = [[0]*n for _ in range(n)]
    group = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                group += 1
                queue = [(i, j)]
                for x, y in queue:
                    for dx, dy in idx:
                        if 0 <= x+dx < n and 0 <= y+dy < n and (area[x][y] == 'R' or area[x][y] == 'G') and (area[x+dx][y+dy] == 'R' or area[x+dx][y+dy] == 'G') and visit[x+dx][y+dy] == 0:
                            visit[x+dx][y+dy] = 1
                            queue.append((x+dx, y+dy))
                        elif 0 <= x+dx < n and 0 <= y+dy < n and area[x][y] == 'B' and area[x+dx][y+dy] == 'B' and visit[x+dx][y+dy] == 0:
                            visit[x+dx][y+dy] = 1
                            queue.append((x+dx, y+dy))
    return group


def color():
    visit = [[0]*n for _ in range(n)]
    group = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                group += 1
                queue = [(i, j)]
                for x, y in queue:
                    for dx, dy in idx:
                        if 0 <= x+dx < n and 0 <= y+dy < n and area[x][y] == area[x+dx][y+dy] and visit[x+dx][y+dy] == 0:
                            visit[x+dx][y+dy] = 1
                            queue.append((x+dx, y+dy))
    return group


n = int(input())
area = [[i for i in input()] for _ in range(n)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(f'{color()} {color_blind()}')