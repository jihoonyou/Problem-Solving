"""
카드
https://www.acmicpc.net/problem/11652
"""
import sys

N = int(sys.stdin.readline())
card_count = {}
curr_max = None
max_cards = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if curr_max is None:
        curr_max = 1
    if num not in card_count:
        card_count[num] = 1
    else:
        card_count[num] += 1
        if card_count[num] > curr_max:
            curr_max = card_count[num]

for key, value in card_count.items():
    if value == curr_max:
        max_cards.append(key)

print(min(max_cards))