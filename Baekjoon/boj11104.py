"""
K번째 수
https://www.acmicpc.net/problem/11004
"""
import sys

N, K = map(int, sys.stdin.readline().split())

sorted_num = sorted(map(int, sys.stdin.readline().split()))

print(sorted_num[K-1])