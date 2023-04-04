a, b, c = map(int, input().split())


if (a == b) and (a == c) and (b == c):
    print(10000+(a*1000))
elif a == b:
    print(1000+a*100)
elif b == c:
    print(1000 + b*100)
elif a == c:
    print(1000 + a*100)
elif a != b and b != c and a != c:
    max_result = max(a, b, c)
    print(max_result*100)
    