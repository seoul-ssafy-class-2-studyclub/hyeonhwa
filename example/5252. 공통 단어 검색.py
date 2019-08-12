T = int(input())
for t in range(T):
    N, M = input().split()
    n = [input() for i in range(int(N))]
    m = [input() for i in range(int(M))]
    result = [i for i in n if i in m]
    print('#{} {}'.format(t+1, len(result)))