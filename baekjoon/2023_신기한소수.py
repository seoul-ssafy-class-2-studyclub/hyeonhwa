def prime(num):
    for i in range(2, int(int(num)**0.5)+1):
        if int(num)%i == 0:
            return
    if len(num) == n:
        print(num)
        return
    for p in prime_nums:
        prime(num+p)

n = int(input())
nums = ['2', '3', '5', '7']
prime_nums = ['1', '3', '7', '9']
for num in nums:
    prime(num)
