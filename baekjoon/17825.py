def bfs(score, n):
    global res
    if n == 10:
        res = max(res, sum(score))
        return
    for i in range(4):
        if visited[i] != 32:
            dice = nums[n]
            if board[visited[i]][dice] == 32:
                temp = visited[i]
                visited[i] = 32
                # print(visited)
                bfs(score, n+1)
                visited[i] = temp
            elif board[visited[i]][dice] not in visited:
                temp = visited[i]
                visited[i] = board[visited[i]][dice]
                # print(visited)
                score[i] += board[visited[i]][0]
                bfs(score, n+1)
                score[i] -= board[visited[i]][0]
                visited[i] = temp
            else:
                continue


nums = list(map(int, input().split()))
board = [
    [0, 1, 2, 3, 4, 5],
    [2, 2, 3, 4, 5, 9],
    [4, 3, 4, 5, 9, 10],
    [6, 4, 5, 9, 10, 11],
    [8, 5, 9, 10, 11, 12],
    [10, 6, 7, 8, 16, 29],
    [13, 7, 8, 16, 29, 30],
    [16, 8, 16, 29, 30, 31],
    [19, 16, 29, 30, 31, 32],
    [12, 10, 11, 12, 13, 17],
    [14, 11, 12, 13, 17, 18],
    [16, 12, 13, 17, 18, 19],
    [18, 13, 17, 18, 19, 20],
    [20, 14, 15, 16, 29, 30],
    [22, 15, 16, 29, 30, 31],
    [24, 16, 29, 30, 31, 32],
    [25, 29, 30, 31, 32, 32],
    [22, 18, 19, 20, 21, 25],
    [24, 19, 20, 21, 25, 26],
    [26, 20, 21, 25, 26, 27],
    [28, 21, 25, 26, 27, 28],
    [30, 22, 23, 24, 16, 29],
    [28, 23, 24, 16, 29, 30],
    [27, 24, 16, 29, 30, 31],
    [26, 16, 29, 31, 31, 32],
    [32, 26, 27, 28, 31, 32],
    [34, 27, 28, 31, 32, 32],
    [36, 28, 31, 32, 32, 32],
    [38, 31, 32, 32, 32, 32],
    [30, 30, 31, 32, 32, 32],
    [35, 31, 32, 32, 32, 32],
    [40, 32, 32, 32, 32, 32],
    [0, 32, 32, 32, 32, 32]
]
res = 0
visited = [0]*4
bfs([0, 0, 0, 0], 0)
print(res)
