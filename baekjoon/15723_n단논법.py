n = int(input())
board = [[1e10]*26 for _ in range(26)]
for __ in range(n):
    string = input()
    s1 = string[0]
    s2 = string[-1]
    board[ord(s1)-97][ord(s2)-97] = 1
for i in range(26):
    board[i][i] = 0
for z in range(26):
    for x in range(26):
        for y in range(26):
            if board[x][y] > board[x][z] + board[z][y]:
                board[x][y] = board[x][z] + board[z][y]
m = int(input())
for _ in range(m):
    string2 = input()
    s3 = string2[0]
    s4 = string2[-1]
    if board[ord(s3)-97][ord(s4)-97] == 1e10:
        print('F')
    else:
        print('T')
