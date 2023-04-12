def solution(my_string):
    # 모음
    gather = ['a', 'e', 'i', 'o', 'u']
    
    for i in gather:
        my_string = my_string.replace(i, '')
    return my_string
    