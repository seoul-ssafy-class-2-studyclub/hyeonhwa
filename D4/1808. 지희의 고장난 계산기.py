# import sys
# sys.stdin = open('지희.txt', 'r')

def check(x):
    cnt = 0
    while x:
        m = x%10
        if board[m] == 0:
            return False
        x //= 10
        cnt += 1
    return cnt


T = int(input())
for t in range(T):
    board = list(map(int, input().split()))
    nums = [i for i in range(10) if board[i] == 1]
    x = int(input())
    if check(x):
        print('#{} {}'.format(t+1, check(x)+1))
    else:
        l = []
        i = 2
        while i < x:
            if check(i) and x%i == 0:
                a = check(i)
                b = check(x//i)
                if a:
                    l += [(i, a)]
                if b:
                    l += [(x//i, b)]
            i += 1
        l.sort(key=lambda x:x[0], reverse=True)
        ans = 0
        flag = 0
        while True:
            if x == 1:
                break
            if x > 1 and flag == 1:
                ans = -1
                break
            for n, cnt in l:
                while x%n == 0:
                    ans += cnt+1
                    x //= n
            flag = 1
        print('#{} {}'.format(t+1, ans))
