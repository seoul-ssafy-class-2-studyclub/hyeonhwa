rect = [list(map(int, input().split())) for i in range(4)]
board = [[0 for i in range(100)] for j in range(100)]


for i in rect:
    newlist = [1 for i in range(i[0],i[2])]
    for j in range(i[1],i[3]):
        board[j][i[0]:i[2]] = newlist

mysum = 0
for i in board:
    mysum += i.count(0)

print(10000-mysum)

