import math

def solution(n):
    # result = n의 제곱근
    result = math.sqrt(n)
    #result가 정수형이 아니면 제곱근 x
    if result != int(result):
        return 2
    else:
        return 1