import sys
sys.stdin = open('1211.txt', 'r')

for t in range(10):
    N = int(input())
    board = [[i for i in input().split()] for j in range(100)]
    inx = [i for i in range(len(board[0])) if board[0][i] == '1']
    cnt = {}
    for ix in inx:
        cnt[ix] = 0
    for key in cnt.keys():
        l = key
        for i in range(100):
            if l != 0 and board[i][l-1] == '1':
                while l > 0 and board[i][l-1] == '1':
                    l -= 1
                    cnt[key] += 1
                cnt[key] -= 1
            elif l != 99 and board[i][l+1] == '1':
                while l < 99 and board[i][l+1] == '1':
                    l += 1
                    cnt[key] += 1
                cnt[key] -= 1

    for key in cnt.keys():
        if cnt[key] == min(cnt.values()):
            print('#{} {}'.format(t+1, key))
            break
