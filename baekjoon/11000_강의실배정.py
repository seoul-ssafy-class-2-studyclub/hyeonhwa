import sys
input = lambda: sys.stdin.readline().rstrip()

# 우선순위큐
n = int(input())
subject = [list(map(int,input().split())) for _ in range(n)]
subject.sort(key=lambda x:x[0])
finish = [subject[0][1]]
for s, t in subject[1:]:
    if finish[0] > s:
        finish.append(t)
    else:
        finish.pop()
        finish.append(t)
print(finish)

# https://covenant.tistory.com/129