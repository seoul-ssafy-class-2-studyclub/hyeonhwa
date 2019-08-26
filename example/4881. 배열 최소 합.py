def permutation(arr):
    if len(arr) == 1:
        return arr[0]
    res = []
    for i in range(len(arr)):
        for j in range(N):
            remaining = [x for x in arr if x != arr[i]]
            new = permutation(remaining)

            for y in new:
                if new.index(y) != j:
                    res.append([arr[i][j], y])

    return res

T = int(input())
for t in range(T):
    N = int(input())
    n = []
    for _ in range(N):
        n += [list(map(int, input().split()))]
    res = permutation(n)