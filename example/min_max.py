def my_max(a):
    maxvalue = a[0]
    for i in range(1, len(a)):
        if maxvalue < a[i]:
            maxvalue = a[i]
    return maxvalue

def my_min(a):
    minvalue = a[0]
    for i in range(1, len(a)):
        if minvalue > a[i]:
            minvalue = a[i]
    return minvalue

T = int(input())
for t in range(T):
    N = int(input())
    n = list(map(int, input().split()))
    if 1 <= T <= 50 and 5 <= N <= 1000 and N == len(n):
        print('#{} {}'.format(t+1, my_max(n)-my_min(n)))