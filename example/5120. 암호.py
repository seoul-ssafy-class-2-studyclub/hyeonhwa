def move(arr):
    if M != len(arr):
        arr.insert(M, arr[M-1]+arr[M])
    else:
        arr += [arr[M-1]+arr[0]]
    return arr

    

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    m = M
    nums = list(map(int, input().split()))
    k = 0
    while k < K:
        move(nums)
        M += m
        if M > len(nums):
            M -= len(nums)
        k += 1
    print('#{} {}'.format(t+1, ' '.join(map(str, nums))))