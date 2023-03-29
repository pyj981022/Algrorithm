def solution(phone_number):
    answer = ''
    
    num_len = len(phone_number)
    answer = '*' * (num_len -4)
    answer += phone_number[-4:]
    return answer