def solution(str1, str2):
    answer = ''
    # str1과 str2의 길이를 더한 만큼을 범위로 잡고
    for i in range(len(str1)+len(str2)):
        # i가 str1 길이의 숫자보다 작을 때 
        if i < len(str1):
            # i에 해당하는 str1의 인덱스 자리를 더하기
            answer += str1[i]
        if i < len(str2):
            answer += str2[i]

    return answer