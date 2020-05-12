def arrive(x=0, y=0, base=0, cnt=0):
    pass


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
idx = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
visit = [[False]*W for _ in range(H)]
visit[0][0] = True
res = 987654321
arrive()
print(res)