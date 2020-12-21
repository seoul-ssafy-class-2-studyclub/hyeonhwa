n, m = map(int, input().split())
for x in range(max(n, m), 0, -1):
    if n % x == 0 and m % x == 0:
        n //= x
        m //= x
        break
print(x)
print(x*n*m)
