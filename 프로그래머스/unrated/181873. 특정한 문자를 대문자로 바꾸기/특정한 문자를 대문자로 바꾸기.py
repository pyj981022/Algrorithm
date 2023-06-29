def solution(my_string, alp):
    answer = ''
    result = []
    for i in my_string:
        if i == alp:
            result.append(i.upper())
        else:
            result.append(i)
    return ''.join(result)