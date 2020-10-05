s = input()
res = []
for i in range(len(s)):
    res.append(s[i:])
res.sort()
print('\n'.join(res))