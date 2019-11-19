def arrive(x=0, y=0, base=0, cnt=0):
    global res
    if x == H-1 and y == W-1:
        if cnt < res:
            res = cnt
            return
    if cnt >= res:
        return
    if cnt < res:
        for i in range(len(idx)):
            if i <= 7:
                if base < K:
                    dx, dy = idx[i]
                    if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == 0 and visit[x+dx][y+dy] == False:
                        if x+dx != H-1 and y+dy != W-1 and res <= cnt+1:
                            return
                        visit[x+dx][y+dy] = True
                        arrive(x+dx, y+dy, base+1, cnt+1)
                        visit[x+dx][y+dy] = False
                else:
                    continue
            else:
                dx, dy = idx[i]
                if 0 <= x+dx < H and 0 <= y+dy < W and board[x+dx][y+dy] == 0 and visit[x+dx][y+dy] == False:
                    if x+dx != H-1 and y+dy != W-1 and res <= cnt+1:
                        return
                    visit[x+dx][y+dy] = True
                    arrive(x+dx, y+dy, base, cnt+1)
                    visit[x+dx][y+dy] = False


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
idx = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
visit = [[False]*W for _ in range(H)]
visit[0][0] = True
res = 987654321
arrive()
print(res)