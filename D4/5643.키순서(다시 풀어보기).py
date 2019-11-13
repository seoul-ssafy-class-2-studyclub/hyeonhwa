T = int(input())
for t in range(T):
    N = int(input())
    M = int(input())
    students = [[0 for _ in range(N+1)] for __ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                students[i][j] = 1000000
    for _ in range(M):
        a, b = map(int, input().split())
        students[a][b] = 1
    for k in range(1, N+1):
        for i in range(1, N+1):
             for j in range(1, N+1):
                if students[i][j] > students[i][k] + students[k][j]:
                    students[i][j] = students[i][k] + students[k][j]
    res = 0
    for i in range(1, N+1):
        flag = True
        for j in range(1, N+1):
            if students[i][j] >= 1000000 and students[j][i] >= 1000000:
                flag = False
                break
        if flag == True:
            res += 1
    print(f'#{t+1} {res}')
