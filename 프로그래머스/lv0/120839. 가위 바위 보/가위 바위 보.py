def solution(rsp):
    answer = ''
    # 가위(2) > 바위(0) / 바위(0) > 보(5) / 보(5) > 가위(2)
    result = {'2':'0', '0':'5', '5':'2'}
    
    for i in rsp:
        answer += result.get(i)
    return answer
    
        