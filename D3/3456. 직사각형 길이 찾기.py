T = int(input())
for t in range(T):
    a, b, c = map(int, input().split())
    if a == b:
        print(f'#{t+1} {c}')
    elif a == c:
        print(f'#{t+1} {b}')
    elif b == c:
        print(f'#{t+1} {a}')