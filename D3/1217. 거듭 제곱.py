def mul(a, b):
    if b == 0:
        return 1
    return mul(a, b-1) * a

for t in range(10):
    num = int(input())
    n, m = input().split()
    print('#{} {}'.format(t+1, mul(int(n),int(m))))