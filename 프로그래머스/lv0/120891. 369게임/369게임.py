def solution(order):
    answer = 0
    # order를 문자열로 변환해 list로 변환
    order = list(str(order))
    # 문자열의 list인 order를 int형의 list로 변환
    order1 = list(map(int, order))
    
    for i in order1:
        # 3, 6, 9 안에 있을 때
        if i in [3, 6, 9]:
            answer += 1
    return answer