"""
조합 0의 개수
https://www.acmicpc.net/problem/2004
"""
import sys

def find_count(x, n):
    count = 0
    div_num = n
    while x >= div_num:
        count = count + x // div_num
        div_num = div_num*n
    return count

N, M = map(int, sys.stdin.readline().split())

print(min(find_count(N,2) - find_count(M,2) - find_count(N-M,2), find_count(N,5) - find_count(M,5) - find_count(N-M,5)))