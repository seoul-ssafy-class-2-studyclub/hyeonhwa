T = int(input())
for tc in range(T):
    n, m = list(map(int, input().split()))
    houses = []
    for i in range(n):
        a = list(map(int, input().split()))
        for j in range(n):
            if a[j] == 1:
                houses.append((i, j))

    res = 0
    for i in range(n):
        for j in range(n):
            center_home_length = [0]*((2*n)+1)
            for x, y in houses:
                center_home_length[abs(i-x) + abs(j-y) + 1] += 1
            for k in range(1, (2*n)+1):
                center_home_length[k] += center_home_length[k-1]
                h = center_home_length[k]
                if m*h >= k*k + (k-1)*(k-1):
                    res = max(res, h)

    print(f"#{tc+1} {res}")