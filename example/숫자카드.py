def count(a,x):
    cnt = 0
    for i in a:
        if x == i:
            cnt += 1
    return cnt

def my_max(a):
    maxvalue = a[0]
    for i in range(1, len(a)):
        if maxvalue < a[i]:
            maxvalue = a[i]
    return maxvalue

T = int(input())

if 1 <= T <= 50:
    for t in range(T):
        N = int(input())
        if 5 <= N <= 100:
            ai = list(input())
            count_value = []
            for i in ai:
                count_value += [count(ai, i)]
            for i in ai:
                if my_max(count_value) == count(ai, i):
                    print(i, my_max(count_value))