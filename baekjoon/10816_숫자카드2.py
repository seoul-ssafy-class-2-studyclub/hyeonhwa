import sys
input = lambda: sys.stdin.readline().rstrip()

def find(x, s, e):
    while s < e:
        mid = (s+e)//2
        if cards[mid] == x:
            i, j = 1, 1
            while mid+i < len(cards) and cards[mid+i] == cards[mid]:
                i += 1
            while 0 <= mid-j and cards[mid-j] == cards[mid]:
                j += 1
            return str(i+j-1)
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
res = {}
for num in cards:
    if num not in res:
        res[num] = find(num, 0, len(cards))
print(' '.join(res[x] if x in res else '0' for x in nums))
