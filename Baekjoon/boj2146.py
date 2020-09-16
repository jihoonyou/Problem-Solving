"""
다리 만들기
https://www.acmicpc.net/problem/2146
"""
import sys

N = int(sys.stdin.readline())
country_map = []

for _ in range(N):
    country_map.append(list(map(int,sys.stdin.readline().split())))

print(country_map)