A,B,C = map(int,input().split())

# 맨 뒤의 개행 문자인 '\n'을 기준으로 cut
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')