# # Trie (문자열 검색)

# class Node:
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         self.children = {}


# class Trie:
#     def __init__(self):
#         self.head = Node(None)

#     def insert_str(self, string):
#         cur_node = self.head
#         for s in string:
#             if s not in cur_node.children.keys():
#                 cur_node.children[s] = Node(s)
#             cur_node = cur_node.children[s]
#         if cur_node.children:
#             return False
#         cur_node.data = string
#         return True

    
#     # def search(self, string):
#     #     cur_node = self.head
#     #     for s in string:
#     #         if s not in cur_node.children.keys():
#     #             return False
#     #         else:
#     #             cur_node = cur_node.children[s]
#     #     if cur_node.data == string:
#     #         return True
#     #     return False


#     # def start_with(self, prefix):
#     #     cur_node = self.head
#     #     words = []
#     #     subtrie = None
#     #     for s in prefix:
#     #         if s in cur_node.children.keys():
#     #             cur_node = cur_node.children[s]
#     #             subtrie = cur_node
#     #         else:
#     #             return []
#     #     cur_nodes = [subtrie]
#     #     next_nodes = []
#     #     while True:
#     #         for s in cur_nodes:
#     #             if s.data != None:
#     #                 words.append(s.data)
#     #             next_nodes += list(s.children.values())
#     #         if len(next_nodes) == 0:
#     #             break
#     #         else:
#     #             cur_nodes = next_nodes
#     #             next_nodes = []
#     #     return words


# res = []
# for tc in range(int(input())):
#     phone = [input() for _ in range(int(input()))]
#     phone = sorted(phone, key=lambda x:len(x), reverse=True)
#     trie = Trie()
#     for i in phone:
#         tf = trie.insert_str(i)
#         if tf == False:
#             break
#     if tf == False:
#         res.append('NO')
#     else:
#         res.append('YES')
# print('\n'.join(res))

import sys
def input(): return sys.stdin.readline()[:-1]

res = []

for tc in range(int(input())):
    phone = [input() for _ in range(int(input()))]
    phone.sort()
    for i in range(len(phone)-1):
        if len(phone[i]) < len(phone[i+1]) and phone[i] == phone[i+1][:len(phone[i])]:
            res.append('NO')
            break
    else:
        res.append('YES')
print('\n'.join(res))
