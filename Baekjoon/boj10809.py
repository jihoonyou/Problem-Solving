"""
알파벳 찾기
https://www.acmicpc.net/problem/10809
"""
import sys

S = sys.stdin.readline().strip()
alphabets = [-1]*26

for idx, alphabet in enumerate(S):
    alphabet_ascii = ord(alphabet) - 97
    if alphabets[alphabet_ascii] == -1:
        alphabets[alphabet_ascii] = idx

for count in alphabets:
    print(count, end= ' ')