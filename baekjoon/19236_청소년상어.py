from copy import deepcopy

def fish_move(sx, sy):
    for i in range(1, 17):
        if location[i]:
            x, y = location[i][0], location[i][1]
            for _ in range(9):
                dx, dy = idx[fishes[x][y][1]-1]
                nx, ny = x+dx, y+dy
                if not 0 <= nx < 4 or not 0 <= ny < 4 or (nx == sx and ny == sy):
                    fishes[x][y][1] = (fishes[x][y][1]+1) % 8
                    continue
                if fishes[nx][ny]:
                    location[fishes[nx][ny][0]] = [x, y]
                fishes[nx][ny], fishes[x][y] = fishes[x][y], fishes[nx][ny]
                location[i] = [nx, ny]
                break


def shark_move(total, direction, x=0, y=0):
    global res, fishes, location
    fish_move(x, y)
    dx, dy = idx[direction]
    while True:
        nx, ny = x+dx, y+dy
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            res = max(res, total)
            return
        if not fishes[nx][ny]:
            x, y = nx, ny
            continue
        temp_fishes, temp_loc = deepcopy(fishes), deepcopy(location)
        temp1, temp2 = fishes[nx][ny], location[fishes[nx][ny][0]]
        location[fishes[nx][ny][0]], fishes[nx][ny] = [], []
        shark_move(total+temp1[0], temp1[1]-1, nx, ny)
        fishes, location = temp_fishes, temp_loc
        location[fishes[nx][ny][0]], fishes[nx][ny] = temp2, temp1
        x, y = nx, ny


fishes = [[] for _ in range(4)]
location = [0]*17
for j in range(4):
    fish_info = list(map(int, input().split()))
    for i in range(0, 8, 2):
        location[fish_info[i]] = [j, i//2]
        fishes[j].append(fish_info[i:i+2])
#  ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
idx = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
res = 0
first = fishes[0][0]
location[fishes[0][0][0]] = []
fishes[0][0] = []
shark_move(first[0], first[1]-1)
print(res)