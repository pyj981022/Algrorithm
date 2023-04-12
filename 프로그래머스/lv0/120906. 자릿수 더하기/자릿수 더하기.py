def solution(n):
    # 입력값 n을 list에 저장하기 위해 문자열로 변환
    n = str(n)
    lst = []
    answer = 0
    
    for i in n:
        # list에 저장 후 
        lst.append(i)
        # i를 int로 변환해 answer에 더하기
        answer += int(i)
    return answer
        