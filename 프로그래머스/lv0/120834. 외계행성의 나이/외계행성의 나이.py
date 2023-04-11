import string
def solution(age):
    answer = ''
    # 소문자 불러오는 라이브러리
    alphabet_lower = list(string.ascii_lowercase)
    # j까지 alp_lower 리스트에 저장
    alp_lower = alphabet_lower[:10]
    
    # age를 str형으로 변환해 요소 하나씩 i에 적용시킨다.
    for i in str(age):
        # i를 int형으로 변환해 인덱싱이 가능하도록 해준다.
        answer += alp_lower[int(i)]
    return answer
    
    
