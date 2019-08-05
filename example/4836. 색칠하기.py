T = int(input())
for t in range(T):
    N = int(input())
    arr = [[0 for i in range(10)] for j in range(10)]
    for n in range(N):
        term = list(map(int, input().split()))
        if term[-1] == 1:
            for i in range(term[0], term[2]+1):
                for j in range(term[1],term[3]+1):
                    arr[i][j] += 1
        if term[-1] == 2:
            for i in range(term[0], term[2]+1):
                for j in range(term[1],term[3]+1):
                    arr[i][j] += 2
    cnt = 0
    for i in arr:
        cnt += i.count(3)
    print('#{} {}'.format(t+1,cnt))
