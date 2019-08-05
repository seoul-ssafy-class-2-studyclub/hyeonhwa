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
if 1<= T <= 50:
    for t in range(T):
        N, M = input().split()
        ai = list(map(int, input().split()))
        if 10 <= int(N) <= 100 and 2 <= int(M) <= int(N) and len(ai) == int(N):
            value = []
            for n in range(int(N) - int(M) + 1):
                a = 0
                for m in range(int(M)):
                    a += ai[n+m]
                value.append(a)
            print('#{} {}'.format(t+1, my_max(value)-my_min(value)))
