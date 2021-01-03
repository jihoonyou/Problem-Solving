'''
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
'''
from collections import deque
def solution(bridge_length,weight,truck_weights):
    answer = 0
    bridge_on = deque([0]* bridge_length)
    truck_q = deque(truck_weights)
    current_weight = 0
    while truck_q:
        answer += 1
        bridge_out = bridge_on.popleft()
        current_weight -= bridge_out
        
        if current_weight + truck_q[0] > weight:
            bridge_on.append(0)
        else:
            truck = truck_q.popleft()
            bridge_on.append(truck)
            current_weight += truck
    while current_weight > 0:
        answer += 1
        bridge_out = bridge_on.popleft()
        current_weight -= bridge_out            
    return answer