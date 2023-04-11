def solution(my_string, n):
    lst = []
    lst2 = []
    for i in my_string:
        lst.append(i)
    for a in lst:
        b = a*n
        lst2.append(b)
    return ''.join(lst2)