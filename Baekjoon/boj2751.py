"""
수 정열하기 2
https://www.acmicpc.net/problem/2751
"""
N = int(input()) 

nums = [] 

for _ in range(N): 
    nums.append(int(input())) 
     
for i in sorted(nums): 
    print(i)