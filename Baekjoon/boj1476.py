"""
날짜 계산
https://www.acmicpc.net/problem/1476
"""
import sys
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
E, S, M = map(int, sys.stdin.readline().split())
e, s, m, junkyu_year = 1, 1, 1, 1
while E != e or M != m or S != s:
    e += 1
    m += 1
    s += 1
    junkyu_year += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

print(junkyu_year)

# 왜 brute-force가 가능한지 https://hjp845.tistory.com/65
# O(1) solution https://codedrive.tistory.com/152