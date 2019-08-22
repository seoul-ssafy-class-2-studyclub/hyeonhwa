board = []
for i in range(5):
    board.append(list(map(int, input().split())))

nums = []
for i in range(5):
    nums += list(map(int, input().split()))

cnt = 0
c1, c2 = 0, 0
for i in nums:
    for j in range(len(board)):
        c = 0
        if i in board[j]:
            k = board[j].index(i)
            board[j][k] = -1
            if board[j].count(-1) == 5:
                cnt += 1
            for s in range(5):
                if board[s][k] > 0:
                    break
                else:
                    c += 1
                    if c == 5:
                        cnt += 1
            if j == k:
                board[j][k] = -1
                c1 -= 1
                if c1 == -5:
                    cnt += 1
            if j == 4-k:
                board[j][k] = -1
                c2 -= 1
                if c2 == -5:
                    cnt += 1
            break
    if cnt == 3:
        print(nums.index(i)+1)
        break
