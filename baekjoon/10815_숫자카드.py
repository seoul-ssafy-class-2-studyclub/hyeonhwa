def find(x, s, e):
    while s < e:
        mid = (s+e)//2
        if cards[mid] == x:
            return '1'
        elif cards[mid] < x:
            s = mid + 1
        else:
            e = mid
    return '0'


n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
nums = list(map(int, input().split()))
res = []
for num in nums:
    res.append(find(num, 0, len(cards)))
print(' '.join(res))
