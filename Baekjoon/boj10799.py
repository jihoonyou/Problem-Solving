"""
쇠막대기
https://www.acmicpc.net/problem/10799
"""
import sys

rod = sys.stdin.readline().rstrip()
stack = []
count = 0
for idx, parenthesis in enumerate(rod):
    if parenthesis == '(':
        stack.append(parenthesis)
    else:
        if rod[idx-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)

