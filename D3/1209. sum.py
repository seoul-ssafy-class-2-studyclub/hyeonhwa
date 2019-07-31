for t in range(10):
    test = int(input())
    n = 100
    l, l2 = [], []
    for i in range(n):
        l1 = list(map(int, input().split()))
        l.append(l1)
    l2 = [[l[j][k]for j in range(len(l))] for k in range(len(l))]
    result = []
    a, b = 0, 0
    for j in range(len(l)):
        result += [sum(l[j])]
        a += l[j][j]
        b += l[j][n-j-1]
        result += [sum(l2[j])]
    result += [a]; result += [b]
    print(f'#{t+1} {max(result)}')