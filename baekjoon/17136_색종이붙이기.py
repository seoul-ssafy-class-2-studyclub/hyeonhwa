import sys
input = lambda: sys.stdin.readline().rstrip()

def one(depth):
    global res, total
    if res > 0 and res <= depth:
        return
    
    if total == 0:
        if res == -1 or res > depth:
            res = depth
        return
    
    for x in range(10):
        for y in range(10):
            if board[x][y]:
                break
        if board[x][y]:
                break
    
    for i in range(1, 6):
        if nums[i] < 5:
            arr = []
            if iscovor(x, y, i):
                for xx in range(x, x+i):
                    for yy in range(y, y+i):
                        arr.append((xx, yy))
                        board[xx][yy] = 0
                total -= i**2
                nums[i] += 1
                one(depth+1)
                total += i**2
                nums[i] -= 1
                for xx, yy in arr:
                    board[xx][yy] = 1


def iscovor(x, y, m):
    for i in range(x, x+m):
        for j in range(y, y+m):
            if 0 <= i < 10 and 0 <= j < 10:
                if not board[i][j]:
                    return False
            else:
                return False
    return True
    

board = [list(map(int, input().split())) for _ in range(10)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[0]*10 for _ in range(10)]
res = -1
nums = [0, 0, 0, 0, 0, 0]
total = sum([sum(m) for m in board])
one(0)
print(res)
