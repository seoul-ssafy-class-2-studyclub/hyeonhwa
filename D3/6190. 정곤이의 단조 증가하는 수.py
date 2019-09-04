# def comb(arr=[], k=0):
#     if len(arr) == 2:
#         res.append(arr)
#         return 0
#     for i in range(k+1, N+1):
#         comb(arr+[i], i)

def plus(x):
    m = x % 10
    x //= 10
    while x:
        if x % 10 > m:
            return False
        m = x % 10
        x //= 10
    return True


T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    ms = -1
    for i in range(N):
        for j in range(i+1, N):
            x = nums[i] * nums[j]
            if ms > x:
                continue
            if plus(x) and ms < x:
                ms = x
    print('#{} {}'.format(t+1, ms))
 