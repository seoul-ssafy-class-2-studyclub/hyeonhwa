import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
words = [input() for _ in range(n)]
res = 0
for word in words:
    check = True
    alpha = [word[0]]
    for w in range(1, len(word)):
        if word[w] not in alpha:
            alpha.append(word[w])
        elif word[w-1] == word[w]:
            continue
        else:
            check = False
            break
    if check:
        res += 1
print(res)