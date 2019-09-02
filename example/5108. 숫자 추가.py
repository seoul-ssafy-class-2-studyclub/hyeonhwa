T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))
    plus = [list(map(int, input().split()))for _ in range(M)]
    for i in plus:
        num.insert(i[0], i[1])
    print('#{} {}'.format(t+1, num[L]))