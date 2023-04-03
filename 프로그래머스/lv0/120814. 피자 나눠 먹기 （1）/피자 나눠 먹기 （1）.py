def solution(n):
    result = n%7
    result_a = n//7
    if result == 0: # 7의 배수일 때
        return result_a # 입력된 n을 7로 나눈 몫 출력
    else: # 7의 배수가 아닐 때
        return result_a+1 # 입력된 n을 7로 나눈 몫에서 1 더하기
