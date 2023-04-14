from collections import Counter

def solution(i, j, k):
    answer = 0
    lst = []
    # i부터 j까지의 범위 내에 있는 모든 한 글자씩을 lst에 저장
    for a in range(i, j+1):
        a = str(a)
        lst.append(a)
    # b가 lst의 원소일 때
    for b in lst:
        k = str(k)
        # b를 찾아 계산
        cnt = Counter(b)
        # k의 개수를 더한 만큼 answer에 저장
        answer += cnt[k]
    return answer 