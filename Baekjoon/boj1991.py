"""
트리 순회
https://www.acmicpc.net/problem/1991
"""
import sys

N = int(sys.stdin.readline())

# class Node:
#     def __init__(self, data, left, right):
#         self.data = data
#         self.left = left
#         self.right = right
# root left right
def pre_order(node):
    if node != '.':
        print(node, end='')
        pre_order(tree[node][0])
        pre_order(tree[node][1])
    
# left root right
def in_order(node):
    if node != '.':
        in_order(tree[node][0])
        print(node, end='')
        in_order(tree[node][1])

# left right root
def post_order(node):
    if node != '.':
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end='')
tree = {}

for _ in range(N):
    data, left, right  = sys.stdin.readline().split()
    tree[data] = [left,right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')
