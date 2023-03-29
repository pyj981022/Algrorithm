def solution(n):
    answer = []
    result = reversed(str(n))
    for i in result:
        answer.append(int(i))
    return answer