n = int(input())
if n <= 1:
    print(n)
else:
    ans = 0
    fibo1 = 0
    fibo2 = 1
    for i in range(2, n+1):
        ans = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = ans
    print(ans)