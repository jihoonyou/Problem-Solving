'''
H-index
https://programmers.co.kr/learn/courses/30/lessons/42747
'''
def solution(citations):
    sorted_citations = sorted(citations)
    
    for i,v in enumerate(sorted_citations):
        if v >= len(sorted_citations) - i:
            return len(sorted_citations) - i
    return 0