def solution(my_string, n):
    # 입력받은 my_string값 중 한 자씩 lst에 저장
    lst = []
    # n번 곱한 값을 lst2에 저장
    lst2 = []
    # my_string의 한 글자씩 lst에 저장
    for i in my_string:
        lst.append(i)
    # 한 글자씩 n번 곱한 것을 lst2에 저장
    for a in lst:
        b = a*n
        lst2.append(b)
    # 최종적으로 lst2의 원소들을 join해 
    return ''.join(lst2)
