def solution(n):
    answer = 0
    
    for i in range(n + 1):
        # i가 2의 배수일 때
        if i % 2 == 0:
            # 0으로 초기화한 answer 값에 i를 더한다.
            answer += i        
    
    return answer