def ind(a, x):
    idx = 0
    for i in a:
        if i != x:
            idx += 1
        else:
            break
    return idx

l = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
ls = [j for i in l for j in i]
basic, n = 0, 5
result = [[0 for i in range(n)] for j in range(n)]
while n > 0:
    for i in range(basic, n+basic):
        a = min(ls)
        result[basic][i] = a
        ls[ind(ls, a)] = 26
    for i in range(basic+1, n+basic):
        a = min(ls)
        result[i][n+basic-1] = a
        ls[ind(ls, a)] = 26
    for i in range(n+basic-2, basic-1, -1):
        a = min(ls)
        result[n+basic-1][i] = a
        ls[ind(ls, a)] = 26
    for i in range(n+basic-2, basic, -1):
        a = min(ls)
        result[i][basic] = a
        ls[ind(ls, a)] = 26
    n -= 2
    basic += 1
# print(result)
    
# delta_x = [0, 1, 0, -1]
# delta_y = [1, 0, -1, 0] # 오른쪽, 아래, 왼쪽, 위 의미
# delta의 인덱스가 벗어나는 순간 0으로 다시 돌아가게 함(4가 되는 순간 4%4 를 통해서!)
# dir_state를 4로 모듈화