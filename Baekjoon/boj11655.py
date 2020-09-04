"""
ROT13
https://www.acmicpc.net/problem/11655
"""
import sys
ROT13 = 13

S = sys.stdin.readline()

for alphabet in S:
    alphabet_ascii = ord(alphabet)
    if alphabet_ascii < 65:
        print(chr(alphabet_ascii), end= '')
    elif alphabet_ascii <= 77:
        print(chr(alphabet_ascii+ROT13), end= '')
    elif alphabet_ascii <= 90:
        print(chr(alphabet_ascii-ROT13), end= '')
    elif alphabet_ascii < 97:
        print(chr(alphabet_ascii), end= '')
    elif alphabet_ascii <= 109:
        print(chr(alphabet_ascii+ROT13), end= '')
    elif alphabet_ascii <= 122:
        print(chr(alphabet_ascii-ROT13), end= '')
    else:
        print(chr(alphabet_ascii), end= '')