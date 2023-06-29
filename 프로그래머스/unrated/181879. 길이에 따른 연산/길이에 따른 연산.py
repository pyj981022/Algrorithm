# prod : 리스트의 모든 요소 곱하는 함수
from math import prod
def solution(num_list):
    answer = 0
    # num_list의 길이가 11이상일 때
    if len(num_list) >= 11:
        # 모든 요소를 다 더하기
        return sum(num_list)
    else:
        # 모든 요소 곱하기
        return prod(num_list)