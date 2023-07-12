def solution(my_string, overwrite_string, s):
    answer = ''
    # my_string의 s부터 끝까지의 글자가 overwrite_string의 길이보다 클 때
    if len(my_string[s:]) > len(overwrite_string):
        answer = my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]
    else:
        answer = my_string[0:s] + overwrite_string
        
    return answer 