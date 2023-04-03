def solution(slice, n):
    answer = n // slice
    answer_result = n % slice
    # answer_result가 n의 배수일 때 몫 출력
    if answer_result == 0:
        return answer
    # 그렇지 않다면 +1해서 출력
    else:
        return answer+1
        