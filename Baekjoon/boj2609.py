"""
최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609
"""
import sys

X, Y = map(int, sys.stdin.readline().strip().split())

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

print(gcd(X,Y))
print(lcm(X,Y))