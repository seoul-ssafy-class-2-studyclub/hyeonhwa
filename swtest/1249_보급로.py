T = int(input())
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for t in range(T):
    N = int(input())
    board = [[int(i) for i in input()] for _ in range(N)]