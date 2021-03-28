def solve(s1, s2, x):
    global res
    r1, r2 = 0, 0
    for i in range(s1, s1+x):
        for j in range(s2, s2+x):
            if board[i][j] == '1':
                r1 += 1
            else:
                r2 += 1
    if not r1:
        res += '0'
        return
    if not r2:
        res += '1'
        return
    res += '('
    solve(s1, s2, x//2)
    solve(s1, s2+x//2, x//2)
    solve(s1+x//2, s2, x//2)
    solve(s1+x//2, s2+x//2, x//2)
    res += ')'


n = int(input())
board = [[i for i in input()] for _ in range(n)]
res = ''
solve(0, 0, n)
print(res)