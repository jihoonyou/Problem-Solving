"""
문자열 분석
https://www.acmicpc.net/problem/10820
"""
import sys

for string in sys.stdin:
    lower_count = 0
    upper_count = 0
    number_count = 0
    space_count = 0
        
    for char in string:
        if 'a' <= char <= 'z':
            lower_count += 1
        elif 'A' <= char <= 'Z':
            upper_count += 1
        elif '0' <= char <= '9':
            number_count += 1
        elif char == ' ':
            space_count += 1

    print(lower_count, upper_count, number_count, space_count)
