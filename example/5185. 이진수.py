def c2(x):
    a = []
    while x:
        a.insert(0, x%2)
        x //= 2
    if len(a) <= 3:
        while len(a) < 4:
            a.insert(0, 0)
    return ''.join(list(map(str, a)))


T = int(input())
for t in range(T):
    N, num = input().split()
    num = [i for  i in num]
    nums = []
    number = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in num:
        if i in number:
            nums.append(number[i])
        else:
            nums.append(int(i))
    for i in range(len(nums)):
        x = c2(nums[i])
        # print(x)
        nums[i] = x
    print('#{} {}'.format(t+1, ''.join(nums)))
    
