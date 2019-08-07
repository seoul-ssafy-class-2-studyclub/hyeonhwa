T = int(input())
for t in range(T):
    N = int(input())
    pascal = [[0]*(i+1) for i in range(N)]
    for i in pascal:
        i[0], i[-1] = 1, 1
    for i in range(2, N):
        for j in range(1, len(pascal[i])-1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    print('#{}'.format(t+1))
    for i in pascal:
        print(' '.join(map(str, i)))
