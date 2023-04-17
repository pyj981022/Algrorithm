def solution(numbers):
    answer = 0
    # check_list: 0~9까지의 범위
    check_list = range(10)
    
    for i in check_list:
        # 확인하는 i가 numbers에 없을 때 answer에 더해줌
        if i not in numbers:
            answer += i
            
    return answer