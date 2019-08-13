T = int(input())
for t in range(T):
    N, A, B = input().split()
    n, a, b = int(N), int(A), int(B)
    r = 0
    mymin = 1000000000
    while r < n:
        for c in range(1, int(n**0.5)+1):
            if n - r * c < 0:
                break
            elif a * abs(r-c) + b * (n - r * c) < mymin:
                mymin = a * abs(r-c) + b * (n - r * c)
        r += 1
    print('#{} {}'.format(t+1,mymin))