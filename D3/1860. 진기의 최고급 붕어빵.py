import sys
sys.stdin = open('1860.txt', 'r')

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_num = [0 for _ in range(max(arrive_time)+1)]
    for i in arrive_time:
        arrive_num[i] += 1
    mk = [0 for i in range(M)]
    for j in range(1, max(arrive_time)//M + 1):
        mk.extend([K*j for i in range(M)])
    result = 'Possible'
    res = [0 for i in range(len(mk))]
    cnt = 0
    for l in range(len(arrive_num)):
        res[l] = mk[l] - arrive_num[l] - cnt
        cnt += arrive_num[l]
        if res[l] < 0:
            result = 'Impossible'
            break
    print('#{} {}'.format(t+1, result))
