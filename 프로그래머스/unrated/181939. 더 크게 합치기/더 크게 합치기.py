def solution(a, b):
    answer = 0
    answer1 = int(str(a) + str(b))
    answer2 = int(str(b) + str(a))
    
    if answer1 > answer2:
        return answer1
    else:
        return answer2
   