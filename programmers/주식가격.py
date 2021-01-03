'''
주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584
'''
def solution(prices):
    answer = [0]*len(prices)
    
    for day in range(len(prices)-1):
        for future in range(day,len(prices)-1):
            if prices[day]  > prices[future]:
                break
            else:
                answer[day] += 1
    return answer