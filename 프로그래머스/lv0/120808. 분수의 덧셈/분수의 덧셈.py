from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    answer = []
    # a, b에 각 분수 설정
    a = Fraction(numer1, denom1)
    b = Fraction(numer2, denom2)
    
    # 분수 더하기
    ans_sum = a + b
    
    # 분수의 분자 설정
    ans_num = ans_sum.numerator
    # 분수의 분모 설정
    ans_den = ans_sum.denominator
    
    answer.append(ans_num)
    answer.append(ans_den)
    
    return answer