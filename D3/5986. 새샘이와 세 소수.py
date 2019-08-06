def primenumber(a):
    i = 2
    while i < a:
        if a % i == 0:
            return False
        i += 1
    return True 

T = int(input())
for t in range(T):
    N = int(input())
    cases = [i for i in range(2, N)]
    case = [i for i in cases if primenumber(i)]
    result = [(x,y,z) for x in case for y in case[case.index(x):] for z in case[case.index(y):] if x + y + z == N]
    print('#{} {}'.format(t+1, len(result)))