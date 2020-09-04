"""
알파벳 개수
https://www.acmicpc.net/problem/10808
"""
import sys

S = sys.stdin.readline().strip()
alphabets = [0]*26

for alphabet in S:
    alphabets[ord(alphabet) - 97] += 1


for count in alphabets:
    print(count, end= ' ')