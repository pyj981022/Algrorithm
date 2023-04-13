def solution(n):
    answer = []
    # 소인수 분해는 2부터 시작
    i = 2
    while i <= n:
        if n % i == 0:
            if i not in answer:
                # i가 n의 소인수일 때, answer에 추가 후 n을 i로 나눈 몫으로 변환
                answer.append(i)
            n //= i
        else:
            i += 1
    return answer