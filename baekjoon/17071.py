import collections

def gosubin():
    queue = collections.deque()
    queue.append(N)
    sis = K
    cnt = 0
    while queue:
        sis += cnt
        if sis > 500000:
            return -1
        for _ in range(len(queue)):
            if cnt % 2 == 0:
                x = queue.popleft()
                if subin1[sis] == True:
                    return cnt
                if 0 <= x-1 and subin2[x-1] == False:
                    queue.append(x-1)
                    subin2[x-1] = True
                if x+1 <= 500000 and subin2[x+1] == False:
                    queue.append(x+1)
                    subin2[x+1] = True
                if 2*x <= 500000 and subin2[2*x] == False:
                    queue.append(2*x)
                    subin2[2*x] = True
            else:
                x = queue.popleft()
                if subin2[sis] == True:
                    return cnt
                if 0 <= x-1 and subin1[x-1] == False:
                    queue.append(x-1)
                    subin1[x-1] = True
                if x+1 <= 500000 and subin1[x+1] == False:
                    subin1[x+1] = True
                    queue.append(x+1)
                if 2*x <= 500000 and subin1[2*x] == False:
                    subin1[x*2] = True
                    queue.append(2*x)
        cnt += 1
    return -1


N, K = map(int, input().split())
subin1 = [False]*500001
subin2 = [False]*500001
if N == K:
    res = 0
else:
    res = gosubin()
print(res)
