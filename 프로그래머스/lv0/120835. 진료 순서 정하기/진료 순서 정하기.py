def solution(emergency):
    answer = []
    # emergency를 내림차순으로 정렬
    tmp = sorted(emergency, reverse=True)
    
    # i가 emergency의 요소일 때
    for i in emergency:
        # answer 리스트에 저장하면서, tmp의 인덱스를 찾아 실제 순위를 찾아준다.
        answer.append(tmp.index(i)+1)
    return answer