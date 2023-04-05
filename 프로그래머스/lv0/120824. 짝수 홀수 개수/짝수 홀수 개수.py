def solution(num_list):
    # answer는 숫자 0과 0으로 이루어진 리스트 생성
    answer = [0, 0]
    
    for i in num_list:
        # i가 짝수일 때, 짝수 자리의 0에 +1
        if i % 2 == 0:
            answer[0] += 1
        # i가 홀수일 때, 홀수 자리의 0에 +1
        else:
            answer[1] += 1
        
        
    return answer