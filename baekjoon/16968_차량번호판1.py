import sys
input = lambda: sys.stdin.readline().rstrip()

s = input()
x = 10
y = 26
if s[0] == 'c':
    res = y
else:
    res = x
for i in range(1, len(s)):
    if s[i] == 'c':
        if s[i-1] == 'c':
            y = 25
        else:
            y = 26
        res *= y
    else:
        if s[i-1] == 'd':
            x = 9
        else:
            x = 10
        res *= x
print(res)