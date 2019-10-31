def change16to10(arr):
    i = 0
    res = 0
    while i < len(arr):
        if arr[len(arr)-i-1] in change.keys():
            x = change[arr[len(arr)-i-1]]
        else:
            x = int(arr[len(arr)-i-1])
        res += x*(16**i)
        i += 1
    return res


T = int(input())
change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
for t in range(T):
    N, K = map(int, input().split())
    n = N//4
    nums = [i for i in input()]
    newnums = nums[:]
    l = []
    for i in range(0, N, n):
        l.append(newnums[i:i+n])
    newnums.insert(0, newnums.pop())
    while nums != newnums:
        for i in range(0, N, n):
            if newnums[i:i+n] not in l:
                l.append(newnums[i:i+n])
        newnums.insert(0, newnums.pop())
    l.sort(key=lambda x:x[:], reverse=True)
    res = change16to10(l[K-1])
    print(f'#{t+1} {res}')
