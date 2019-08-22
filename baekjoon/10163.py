N = int(input())
board = [[0 for _ in range(1001)] for __ in range(1001)]
boxes = []
for i in range(N):
    boxes += [list(map(int, input().split()))]

area = 1
for box in boxes:
    newbox = [area for _ in range(box[0], box[0] + box[2])]
    for b in range(box[1], box[1]+box[3]):
        board[b][box[0]:box[0]+box[2]] = newbox
    area += 1

s = [0 for _ in range(area-1)]

for i in range(1, area):
    for box in board:
        if i in box:
            s[i-1] += box.count(i)

print('{}'.format('\n'.join(list(map(str, s)))))
