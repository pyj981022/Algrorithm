def solution(num_list):
    answer = 0
    answer1 = 1
    for i in num_list:
        answer += i
        a = answer ** 2
    for i in num_list:
        answer1 *= i
    # return answer1
    if answer1 > a:
        return 0
    else:
        return 1