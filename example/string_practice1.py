s = 'Reverse this strings'
result = []
for i in range(len(s)-1, -1, -1):
    result += [s[i]]
print(''.join(result))