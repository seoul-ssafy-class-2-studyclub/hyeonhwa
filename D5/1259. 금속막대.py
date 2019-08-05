T = int(input())
for t in range(T):
    N = int(input())
    l = input().split()
    ls = []
    for i in range(len(l)):
        if i % 2:
            ls += [l[i-1:i+1]]
    a = []
    result = []
    for i in range(len(ls)):
        for j in range(len(ls)):
            if ls[i][0] == ls[j][1]:
                a += [i]
    result = [ls[i] for i in range(N) if i not in a]
    while len(result) < len(ls):
        for i in ls:
            if result[-1][1] == i[0]:
                result.append(i)
        if len(result) == N:
            break
    results = [' '.join(i) for i in result]
    print('#{} {}'.format(t+1, ' '.join(results)))
    
