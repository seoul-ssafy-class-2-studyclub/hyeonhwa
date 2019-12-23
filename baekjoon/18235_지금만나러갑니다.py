N, A, B = map(int, input().split())
fduck = [0]*(N*4)
fduck[1] = A
sduck = [0]*(N*4)
sduck[1] = B
res = 0
k, i = 1, 1
while i < 4*N:
    if fduck[i] != 0:
        if fduck[i] - k > 0:
            fduck[i*2] = fduck[i] - k
        if fduck[i] + k <= N:
            fduck[i*2+1] = fduck[i] + k
    if sduck[i] != 0:
        if sduck[i] - k > 0:
            sduck[i*2] = sduck[i] - k
        if sduck[i] + k <= N:
            sduck[i*2+1] = sduck[i] + k
    i += 1
    if i == k*2:
        flag = 0
        k *= 2
        res += 1
        for j in fduck[i:i*2]:
            if j != 0 and j in sduck[i:i*2]:
                flag = 1
                break
        if flag == 1:
            break
        if fduck[i:i*2].count(0) == k or sduck[i:i*2].count(0) == k:
            res = -1
            break
print(sduck)
print(res)
