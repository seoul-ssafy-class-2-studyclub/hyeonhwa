for t in range(10):
    N = int(input())
    h = list(map(int, input().split(' ')))
    for cnt in range(N):
        h[h.index(max(h))] = max(h) - 1
        h[h.index(min(h))] = min(h) + 1

    print('#{} {}'.format(t+1, max(h)-min(h)))