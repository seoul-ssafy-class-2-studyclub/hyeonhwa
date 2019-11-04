def move():
    for i in range(len(chesses)):
        x+1, y+1, d = chesses.pop(0):
        dx, dy = idx[d]
        if 0 <= x+dx < N and 0 <= y+dy < N and board[x][y] == 0:
            for n, m, red in chesses:
                if x+dx+1 == n and y+dy+1 == m:


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
idx = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
dr = {1:2, 2:1, 3:4, 4:3}
chesses = [list(map(int, input().split())) for _ in range(K)]
k = 0
while k <= 1000:
    move()
    k += 1
