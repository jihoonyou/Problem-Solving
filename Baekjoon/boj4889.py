'''
안정적인 문자열
https://www.acmicpc.net/problem/4889
'''
import sys

brackets = sys.stdin.readline().strip()
trial = 1

while len(brackets) == 0 or brackets[0] != '-':
    left_bracket_stack = []
    swap_count = 0
    
    for bracket in brackets:
        if bracket == '{':
            left_bracket_stack.append(bracket)
        else:
            if not left_bracket_stack:
                left_bracket_stack.append("{")
                swap_count += 1
            else:
                left_bracket_stack.pop()
    
    swap_count += len(left_bracket_stack) // 2
    print(f'{trial}. {swap_count}')

    brackets = sys.stdin.readline().strip()
    trial += 1
