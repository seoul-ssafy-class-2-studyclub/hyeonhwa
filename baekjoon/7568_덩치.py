n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = []
for i in range(len(arr)):
    x1, y1 = arr[i]
    cnt = 1
    for j in range(len(arr)):
        if i != j:
            x2, y2 = arr[j]
            if x1 < x2 and y1 < y2:
                cnt += 1
    ans.append(cnt)
print(*ans)