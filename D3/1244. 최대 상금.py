def change(arr, num1, num2):
    ar = []
    for i in arr:
        ar += [i]
    ar[num1], ar[num2] = ar[num2], ar[num1]
    arr = ''.join(ar)
    return arr


def dp(depth, number):
    if depth == K:
        return number

    if cache[depth].get(number):
        # cache[depth][number]
        return cache[depth][number]

    res = 0
    for [x, y] in cl:
        num = change(number, x, y)
        res = max(res, int(dp(depth+1, num)))

    cache[depth][number] = res

    return res


T = int(input())
for t in range(T):
    n, K = input().split()
    K = int(K)
    cache = [{} for i in range(K+1)]
    cl = []
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            cl.append([i, j])
    print(f'#{t+1} {dp(0,n)}')