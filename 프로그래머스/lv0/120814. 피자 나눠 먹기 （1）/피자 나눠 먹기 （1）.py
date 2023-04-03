def solution(n):
    result = n%7
    result_a = n//7
    if result == 0:
        return result_a
    else:
        return result_a+1