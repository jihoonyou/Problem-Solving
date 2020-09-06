"""
최소공배수
https://www.acmicpc.net/problem/1934
"""
import sys

T = int(sys.stdin.readline())

def gcd(x,y):
    while y != 0:
        if y > x:
            x,y = y,x
        if y == 0:
            return x
        if x % y == 0:
            return y
        x,y = y, x%y

def lcm(x,y):
    return x*y//gcd(x,y)


for _ in range(T):
    X, Y = map(int, sys.stdin.readline().split())
    print(lcm(X,Y))