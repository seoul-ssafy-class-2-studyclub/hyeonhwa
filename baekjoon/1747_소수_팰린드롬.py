def check(num):
    i, j = 0, len(num)-1
    while i < j:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1
    return True


n = int(input())
prime_number = [1]*10000001
prime_number[0], prime_number[1] = 0, 0
i = 2
while i*i <= 10000000:
    if prime_number[i]:
        for j in range(i*i, 10000001, i):
            if prime_number[j]:
                prime_number[j] = 0
    i += 1
x = n
while True:
    if prime_number[x] and check(str(x)):
        print(x)
        break
    x += 1
