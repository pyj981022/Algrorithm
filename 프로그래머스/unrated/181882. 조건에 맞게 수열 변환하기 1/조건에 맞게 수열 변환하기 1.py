def solution(arr):
    answer = []
    for i in arr:
        # 50보다 크거나 같은 짝수일 때
        if i % 2 == 0 and i >= 50:
            # i를 2로 나누기
            answer.append(i/2)
        # 50보다 작은 홀수일 때
        elif i % 2 ==1 and i <= 50:
            # 2를 곱하기
            answer.append(i*2)
        else:
            answer.append(i)
    return answer