from collections import deque

def meet():
    queue1 = deque([A])
    queue2 = deque([B])
    i = 1
    cnt = 0
    while queue1 and queue2:
        if len(queue1) == 0 or len(queue2) == 0:
            return -1
        visit = [0]*(N+1)
        for _ in range(len(queue1)):
            x = queue1.popleft()
            if x - i > 0 and not visit[x-i]:
                queue1.append(x-i)
                visit[x-i] = 1
            if x + i <= N and not visit[x+i]:
                queue1.append(x+i)
                visit[x+i] = 1
        for _ in range(len(queue2)):
            y = queue2.popleft()
            if y - i > 0:
                if not visit[y-i]:
                    queue2.append(y-i)
                    visit[y-i] = 1
                else:
                    return cnt+1
            if y + i <= N:
                if not visit[y+i]:
                    queue2.append(y+i)
                    visit[y+i] = 1
                else:
                    return cnt+1
        i *= 2
        cnt += 1
    return -1
            

N, A, B = map(int, input().split())
if (A % 2 and not B % 2) or (not A % 2 and B % 2):
    res = -1
else:
    res = meet()
print(res)
