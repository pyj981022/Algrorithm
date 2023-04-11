from sys import stdin

# 총 금액
x = int(input())
# 구매한 상품 목록의 개수
n = int(input())
# 합 초기값
sum_price = 0


for i in range(n):
    # 상품 목록만큼 입력받기
    a, b = map(int, input().split())
    # 합 초기값에 a*b한 것을 더하기
    sum_price += a*b

# 총 금액과 상품 총 금액 더한 것과 같으면 Yes
if x == sum_price:
    print("Yes")
else:
    print("No")