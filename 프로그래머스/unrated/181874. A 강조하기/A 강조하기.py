def solution(myString):
    answer = ''
    result = []
    for i in myString:
        if i == 'a':
            result.append(i.upper())
        elif i == 'A':
            result.append(i)
        else:
            result.append(i.lower())
    return "".join(result)