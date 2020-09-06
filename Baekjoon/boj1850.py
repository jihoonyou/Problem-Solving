"""
최대공약수
https://www.acmicpc.net/problem/1850
"""
import sys

def gcd(x,y):
    while y != 0:
        if y > x:
            x,y = y,x
        if y == 0:
            return x
        if x % y == 0:
            return y
        x,y = y, x%y

A,B = map(int,sys.stdin.readline().split())
print('1'*gcd(A,B))