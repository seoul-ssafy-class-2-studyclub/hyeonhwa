import sys
input = lambda: sys.stdin.readline().rstrip()

nums = [int(i) for i in input().split()]

while True:
    for i in range(4):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums) # Asterisk(*) 
    if nums == [1, 2, 3, 4, 5]:
        break