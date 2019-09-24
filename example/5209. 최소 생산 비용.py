def backtrack(arr, x):
    global res
    if sum(arr) >= res:
        return
    if len(arr) == N:
        if res > sum(arr):
            res = sum(arr)
        return
    for i in range(N):
        if i not in visited:
            arr.append(board[x][i])
            visited.append(i)
            backtrack(arr, x+1)
            arr.pop()
            visited.pop()


T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    res = 10000000
    backtrack([], 0)
    print(f'#{t+1} {res}')