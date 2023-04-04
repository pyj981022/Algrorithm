a, b, c = map(int, input().split())

# a, b,c 같은 눈
if (a == b) and (a == c) and (b == c):
    print(10000+(a*1000))
# a와 b가 같은 눈    
elif a == b:
    print(1000+a*100)
# b와 c가 같은 눈    
elif b == c:
    print(1000 + b*100)
# a와 c가 같은 눈    
elif a == c:
    print(1000 + a*100)
# a, b, c 다 다른 눈    
elif a != b and b != c and a != c:
    max_result = max(a, b, c)
    print(max_result*100)
    
