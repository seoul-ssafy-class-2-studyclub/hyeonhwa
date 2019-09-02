T = int(input())
for t in range(T):
    N = int(input())
    ab = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus = []
    for _ in range(P):
        bus += [[int(input()), 0]]
    for a, b in ab:
        for i in bus:
            if a <= i[0] <= b:
                i[1] += 1
    res = [i[1] for i in bus]
    print('#{} {}'.format(t+1, ' '.join(map(str, res))))