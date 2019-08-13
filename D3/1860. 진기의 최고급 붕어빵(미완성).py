import sys
sys.stdin = open('1860.txt', 'r')

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arrive = sorted(list(map(int, input().split())))
    # print(arrive)
    mk = [0 for i in range(max(arrive))]
    cnt = 1
    result = 'Possible'
    for i in range(M, len(mk)+1, M):
        mk[i-1:] = [mk[i-1] + K for j in range(len(mk)-i+1)]
        if mk[i-1] >= N:
            break
    for i in arrive:
        mk[i-1] = mk[i-1] - cnt
        cnt += 1
        if mk[i-1] < 0:
            result = 'Impossible'
            break
    print('#{} {}'.format(t+1, result))
