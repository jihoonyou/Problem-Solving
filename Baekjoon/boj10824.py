"""
네 수
https://www.acmicpc.net/problem/10824
"""
import sys

A,B,C,D = map(str, sys.stdin.readline().split())
x, y = (int(A+B), int(C+D))

print(x+y)