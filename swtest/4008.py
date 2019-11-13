import sys
sys.stdin = open('input6.txt', 'r')

def comb(idx):
    global maxnum
    global minnum
    global num
    if idx >= N:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
        return
    for i in range(len(cals)):
        if cals[i] > 0:
            temp = num
            cals[i] -= 1
            if i == 0:
                num += nums[idx]
            elif i == 1:
                num -= nums[idx]
            elif i == 2:
                num *= nums[idx]
            else:
                if nums[idx] != 0:
                    if num < 0:
                        num = -((-num)//nums[idx])
                    else:
                        num //= nums[idx]
                else:
                    cals[i] += 1
                    continue
            comb(idx+1)
            cals[i] += 1
            num = temp


T = int(input())
for t in range(T):
    N = int(input())
    cals = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    maxnum, minnum = -100000000, 100000000
    num = nums[0]
    comb(1)
    # print(maxnum, minnum)
    print(f'#{t+1} {maxnum-minnum}')
