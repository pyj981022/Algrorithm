def solution(start, end):
    answer = []
    for i in range(end, start+1):
        answer.append(i)
        answer.sort(reverse=True
                   )
    return answer