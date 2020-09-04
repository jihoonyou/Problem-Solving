"""
접미사 배열
https://www.acmicpc.net/problem/11656
"""
import sys

S = sys.stdin.readline().strip()
suffix = []

for idx in range(len(S)):
    suffix.append(S[idx:])

for element in sorted(suffix):
    print(element)