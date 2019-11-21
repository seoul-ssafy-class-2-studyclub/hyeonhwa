def go():
    value, node = P, 1
    cnt = 0
    while True:
        nv, nx = 0, 0
        if value+node >= L-1:
            return cnt
        for j in range(N):
            if node < l[j][0] <= value+node:
                if nv < l[j][1]:
                    nv = l[j][1]
                    nx = l[j][0]
        if (nv, nx) == (0, 0):
            break
        value, node = nv+value-nx, nx
        cnt += 1
    return -1

    

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x:x[0])
L, P = map(int, input().split())
res = go()
print(res)