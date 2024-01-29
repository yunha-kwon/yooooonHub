total_price = int(input())
product_type = int(input())

calculate_price = 0

for i in range(product_type):
    price, num = map(int, input().split())
    calculate_price += (price * num)

if calculate_price == total_price:
    print("Yes")
else:
    print("No")
