N = int(input())
x = 1
while x < N:
    plus = x
    i = x
    while i:
        plus += i%10
        i //= 10
    if plus == N:
        print(x)
        break
    x += 1
if x == N:
    print(0)
