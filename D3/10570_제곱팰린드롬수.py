import math
 
def pal(x):
    i, j = 0, len(x)-1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True
 
 
for t in range(int(input())):
    a, b = map(int, input().split())
    res = 0
    for x in range(a, b+1):
        if pal(str(x)):
            y = math.sqrt(x)
            if int(y) == y:
                y = int(y)
                if pal(str(y)):
                    res += 1
    print(f'#{t+1} {res}')