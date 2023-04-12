def solution(my_string):
    answer = ''
    for i in my_string:
        # i가 대문자이면 소문자로 변환해서 answer에 넣기
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer