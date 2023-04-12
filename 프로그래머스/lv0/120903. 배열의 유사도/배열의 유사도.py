def solution(s1, s2):
    answer = 0
    # i가 s1안에 있을 때
    for i in s1:
        # 만약 i가 s2에 있다면
        if i in s2:
            # answer에 더하기 1
            answer += 1
    return answer