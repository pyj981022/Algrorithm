def solution(arr, divisor):
    answer = []
    # 리스트를 먼저 정렬
    arr.sort()
    for i in arr:
        # 나누어 떨어지면 answer에 추가
        if i % divisor == 0:
            answer.append(i)
    # answer가 비어있다는 것은 나누어 떨어지는 숫자가 없다는 것
    if len(answer) == 0:
        answer = [-1]
    return answer