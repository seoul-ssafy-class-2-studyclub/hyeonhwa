T = int(input())
for t in range(T):
    N = int(input())
    v = [[i for i in input().split()] for j in range(N)]
    v.insert(0, [0, 0])
    l, v1 = 0, 0
    for i in range(1,len(v)):
        if v[i][0] == '1':
            v1 += int(v[i][1])
            l += v1
        elif v[i][0] == '0':
            l += v1
        else:
            v1 -= int(v[i][1])
            if v1 < 0:
                v1 = 0
            l += v1
    print(f'#{t+1} {l}')
            