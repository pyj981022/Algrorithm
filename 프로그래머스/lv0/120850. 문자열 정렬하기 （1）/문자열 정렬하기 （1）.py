import re

def solution(my_string):
    answer = []
    
    # 문자열 내 숫자 찾기
    numbers = re.findall(r'\d', my_string)
    # 문자열로 되어 있는 요소들을 int로 변환
    result = list(map(int, numbers))
    # 정렬
    result.sort()
    return result