def solution(n):
    divisior = []
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisior.append(i)
        answer = sum(divisior)
    return answer
