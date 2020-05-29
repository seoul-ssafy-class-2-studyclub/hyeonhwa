class Node():
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
    
num_list =[1,2,3,4]
temp = Node(num_list[-1], None)

for i in range(len(num_list) - 2, -1, -1):
    temp  = Node(num_list[i], temp)

head = temp

p = head

while p.nxt != None:
    print(p.value)
    p = p.nxt
print(p.value)


p = head

for _ in range(4):
    p = p.nxt

# 삭제
p.nxt = p.nxt.nxt

# 추가
p.nxt = Node(2, p.nxt)
