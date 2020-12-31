'''
시저 암호
https://programmers.co.kr/learn/courses/30/lessons/12926
'''
def solution(s, n):
    answer = ''
    for char in s:
        if ord(char) == 32:
            answer += ' '
        elif 65 <= ord(char) and ord(char) <= 90:
            new_ord = (ord(char)+n)
            if new_ord > 90:
                new_ord = new_ord%90 + 64
            answer += chr(new_ord)
        else:
            new_ord = (ord(char)+n)
            if new_ord > 122:
                new_ord = new_ord%122 + 96
            answer += chr(new_ord)
    return answer