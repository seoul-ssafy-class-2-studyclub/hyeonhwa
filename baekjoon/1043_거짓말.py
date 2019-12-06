from collections import deque

def play():
    queue = deque()
    queue.extend(know)
    while queue:
        x = queue.pop()
        for i in range(M):
            if x in party[i][1:]:
                for j in party[i][1:]:
                    if j not in know:
                        know.append(j)
                        queue.append(j)


N, M = map(int, input().split())
know = list(map(int, input().split()))
know = know[1:]
party = [list(map(int, input().split())) for _ in range(M)]
play()
res = 0
for i in range(M):
    for j in party[i][1:]:
        if j in know:
            break
    else:
        res += 1
print(res)
