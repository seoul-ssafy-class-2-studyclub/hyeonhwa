def find(s, e):
    res = 0
    while s < e:
        mid = (s + e)//2
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree-mid
        if total >= m:
            res = mid
            s = mid + 1
        elif total < m:
            e = mid
    return res


n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(find(0, max(trees)))
