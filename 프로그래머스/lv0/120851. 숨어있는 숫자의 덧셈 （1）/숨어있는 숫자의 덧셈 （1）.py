import re


def solution(my_string):
    # 숫자를 더하기 위해 초기화
    answer = 0
    
    # 입력값 my_string 내 모든 숫자 찾기
    numbers = re.findall(r'\d', my_string)
    # 숫자 list를 int형으로 변환
    result = list(map(int, numbers))
    
    # 숫자로 변환된 list의 요소 합
    for i in result:
        answer += i
    return answer
