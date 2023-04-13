def solution(my_string):
    answer = ''
    # 소문자로 바꾸기
    my_string = my_string.lower()
    # 정렬 → str형은 sort() 메소드가 없기 때문에 sorted() 사용
    answer = ''.join(sorted(my_string))
    return answer