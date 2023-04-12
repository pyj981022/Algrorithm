from math import factorial as fac

def solution(balls, share):
    # n!
    n = fac(balls) 
    # m!
    m = fac(share)
    
    answer = n/(fac(balls-share)*m)
    
    
    
    
    return answer