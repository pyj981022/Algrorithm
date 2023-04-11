def solution(n, k):
    n1 = n // 10
    # n이 10이상일 때 적용되는 가격 식
    answer = n*12000 + k*2000 - n1*2000
    # n이 10이하일 때 적용되는 가격 식
    answer2 = n*12000 + k*2000
    
    if n >= 10:
        return answer
    else:
        return answer2