def solution(array):
    answer = []
    max_array = max(array)
    for i in array:
        if i ==  max_array:
            # 여러 값을 list에 한 번에 넣을 때 extend 사용
            # array.index(i) = i의 인덱스 위치를 찾아준다.
            answer.extend([i, array.index(i)])

    return answer