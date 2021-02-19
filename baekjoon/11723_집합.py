import sys

nums = []
for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().rstrip().split()
    if len(x) == 1:
        if x[0] == 'all':
            nums = [i for i in range(1, 21)]
        elif x[0] == 'empty':
            nums = []
    else:
        y, x = int(x[1]), x[0]
        if x == 'add':
            if y not in nums:
                nums.append(y)
        elif x == 'remove':
            if y in nums:
                nums.remove(y)
        elif x == 'check':
            print(1 if y in nums else 0)
        elif x == 'toggle':
            if y in nums:
                nums.remove(y)
            else:
                nums.append(y)
