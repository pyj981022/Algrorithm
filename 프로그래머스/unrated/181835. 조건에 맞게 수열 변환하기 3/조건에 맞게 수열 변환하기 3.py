def solution(arr, k):
    answer = []
    
    # i가 arr의 원소일 때
    for i in arr:
        # k → 짝수
        if k % 2 == 0:
            answer.append(i+k)
        # k → 홀수
        else:
            answer.append(i*k)
        
    return answer