numbers = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
T = int(input())
for t in range(T):
    N = input().split()
    nums = input().split()
    number = [numbers[num] for num in nums]
    number.sort()
    num = [key for i in number for key, value in numbers.items() if i == value]
    print('#{}'.format(t+1))
    for i in num:
        print(i, end=' ')