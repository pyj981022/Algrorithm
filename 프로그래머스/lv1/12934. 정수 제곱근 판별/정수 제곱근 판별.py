import math

def solution(n):
    answer = math.sqrt(n)
    if int (answer) == answer:
        return (answer+1)**2
    else: 
        return -1
    
    # return answer