n = int(input())
words = [[i for i in input()] for _ in range(n)]
x = 9
nums = {}
for word in words:
    for i in range(len(word)):
        if word[i] in nums:
            nums[word[i]] += 10**(len(word)-i-1)
        else:
            nums[word[i]] = 10**(len(word)-i-1)
chars = sorted(nums.items(), key=lambda x:x[1], reverse=True)
x = 9
res = 0
for key, value in chars:
    res += x*value
    x -= 1
print(res)
