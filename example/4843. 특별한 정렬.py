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
    result = []
    l = len(n)
    for i in range(len(n)):
        if len(l) > 1:
            result.append(my_max(n))
            n.remove(my_max(n))
            result.append(my_min(n))
            n.remove(my_min(n))
        elif len(n) == 1:
            result.append(n[0])
            break
        else:
            break

    print(f'#{t+1} {" ".join(list(map(str, result[:10])))}')
