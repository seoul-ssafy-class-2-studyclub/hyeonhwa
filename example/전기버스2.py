def my_max(a):
    maxvalue = a[0]
    for i in range(1, len(a)):
        if maxvalue < a[i]:
            maxvalue = a[i]
    return maxvalue

def l(numbers, x):
    number = []
    result = 1
    for i in range(len(numbers)-1):
        if  numbers[i] == numbers[i+1] and numbers[i] == x:
            result += 1
        if numbers[i] != numbers[i+1]:
            result = 1
        number.append(result)
    return my_max(number)

def count(a,x):
    cnt = 0
    for i in a:
        if x == i:
            cnt += 1
    return cnt

T = int(input())
if 1 <= T <= 50:
    for t in range(T):
        K, N, M = input().split()
        m = list(map(int, input().split()))
        if len(m) == int(M):
            n = [0 for i in range(int(N))]
            for i in m:
                n[i] = 1
            cnt = 0
            if l(n, 0) >= int(K):
                cnt = 0
            else:
                nn = []
                x = 0
                while x < int(N) - int(K):
                    nn.append(n[x+1: x+int(K)+1])
                    if count(n[x+1: x+int(K)+1], 1) > 1:
                        x = n[x+1: x+int(K)+1].index(1, n[x+1: x+1+int(K)].index(1)+1) + x + 1
                    else:
                        if 1 in n[x+1: x+1+int(K)]:
                            x += n[x+1: x+1+int(K)].index(1) + 1
                for i in nn:
                    print(nn)
                    if 1 in i:
                        cnt += 1
            print('#{} {}'.format(t+1,cnt))
