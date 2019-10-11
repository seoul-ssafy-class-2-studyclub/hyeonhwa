def init(idx):
    global cnt

    if idx * 2 <= N:
        init(2 * idx)
    
    binary_tree[idx] = cnt
    cnt += 1
    print(binary_tree)

    if idx * 2 + 1 <= N:
        init(2 * idx + 1)

            
for t in range(int(input())):
    N = int(input())
    binary_tree = [0] * (N + 1)
    cnt = 1
    init(1)
    print('#%d %d %d' %(t + 1, binary_tree[1] ,binary_tree[N // 2]))