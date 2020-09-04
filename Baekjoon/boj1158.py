"""
요세푸스 문제
https://www.acmicpc.net/problem/1158
"""
import sys

N, K = map(int, sys.stdin.readline().split())
input_list = list(range(1, N+1))
josephus_permutation = []
step = 0

while input_list:
    step = (step + (K - 1)) % len(input_list)
    josephus_permutation.append(input_list.pop(step))

print('<' + ', '.join(str(x) for x in josephus_permutation) + '>')
