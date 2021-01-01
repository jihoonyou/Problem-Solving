'''
문자열 다루기 기본
https://programmers.co.kr/learn/courses/30/lessons/12918
'''
def solution(s):
    if len(s) ==4 or len(s) == 6:
        for char in s:
            if ord('0') > ord(char) or ord('9') < ord(char):
                return False
        return True
    return False
# return s.isdigit() and len(s) in (4, 6)