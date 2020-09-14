import sys
input = lambda: sys.stdin.readline().rstrip()

def calc(x, y, string):
    if len(string) == 6:
        if string not in nums:
            nums.append(string)
        return
    for dx, dy in idx:
        if 0 <= x+dx < 5 and 0 <= y+dy < 5:
            calc(x+dx, y+dy, string+board[x+dx][y+dy])

board = [list(input().split()) for _ in range(5)]
idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
nums = []
for x in range(5):
    for y in range(5):
        calc(x, y, board[x][y])
print(len(nums))