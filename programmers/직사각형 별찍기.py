'''
직사각형 별찍기
https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3
'''
a, b = map(int, input().strip().split(' '))
stars = a*'*'
for _ in range(b):
    print(stars)