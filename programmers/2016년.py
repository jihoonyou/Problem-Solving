'''
2016년
https://programmers.co.kr/learn/courses/30/lessons/12901
'''
def solution(a, b):
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = b
    for i in range(a-1):
        days += month[i]
    return day[days%7]