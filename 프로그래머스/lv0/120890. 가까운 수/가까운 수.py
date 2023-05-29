def solution(array, n):
    box = []
    # array를 정렬
    array.sort()
    
    # i가 array의 원소일 때
    for i in array:
        # box에 추가한다. 단 n에서 i를 뺀 값의 절댓값을
        box.append(abs(n-i))
    # box에서 가장 작은 값의 index 숫자를 array에 index로 찾는다
    answer = [array[box.index(min(box))]]
    # answer의 값이 2개부터일 때
    if len(answer) > 1:
        # 그 중 가장 작은 값을 return한다.
        return min(answer)
    else:
        return answer[0]