a = int(input())
b = input()

# b를 문자열로 입력받아 indexing으로 각 자리를 곱해준다.
a3 = a*int(b[2])
a4 = a*int(b[1])
a5 = a*int(b[0])
a6 = a*int(b)

print(a3, a4, a5, a6, sep='\n')