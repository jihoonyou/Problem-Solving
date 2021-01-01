'''
모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840
'''
def solution(answers):
    answer = []
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0]*3

    for index, element in enumerate(answers):
        if element == student1[index%len(student1)]:
            score[0] +=1
        if element == student2[index%len(student2)]:
            score[1] +=1
        if element == student3[index%len(student3)]:
            score[2] +=1

    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
    return answer
