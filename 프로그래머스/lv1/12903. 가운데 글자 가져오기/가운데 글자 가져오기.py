def solution(s):
    answer = ''
    # s의 길이가 홀수일 때 
    if len(s) % 2 == 1:
        # s의 길이를 2로 나눈 값을 인덱스로 해 출력
        return s[len(s)//2]
    else:
        # s의 길이가 홀수일 때, 반으로 나누고 그 앞자리와 뒷자리를 출력
        return s[(len(s)//2-1):(len(s)//2+1)]