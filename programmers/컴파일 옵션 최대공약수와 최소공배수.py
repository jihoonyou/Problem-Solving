'''
최대공약수와 최소공배수
https://programmers.co.kr/learn/courses/30/lessons/12940
'''
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a % b)
def lcm(a,b):
    return a*b // gcd(a,b)
def solution(n, m):
    return [gcd(n,m),lcm(n,m)]