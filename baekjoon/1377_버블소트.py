import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [(int(input()), i) for i in range(n)]

# 버블정렬 -> o(n2)의 시간복잡도
# change = False
# for i in range(n):
#     change = False
#     for j in range(n-(i+1)):
#         if a[j] > a[j+1]:
#             change = True
#             a[j], a[j+1] = a[j+1], a[j]
#     if change == False:
#         print(i+1)
#         break

# 횟수 = index 값 비교
sa = sorted(a)
ans = 0
for i in range(n):
    ans = max(ans, sa[i][1]-a[i][1])
print(ans+1)