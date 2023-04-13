def solution(n):
    answer = 0
    result = []
    # 2~ n의 약수 개수 
    for i in range(2, n+1):
        for j in range(1, i+1):
            
            if i % j == 0:
                result.append(i)
        if result.count(i) >= 3:
            answer += 1
    return answer