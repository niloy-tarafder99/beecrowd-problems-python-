item1 = input().split(" ")
item2 = input().split(" ")

code1, quantity1, price1 = item1
code2, quantity2, price2 = item2

total_price = (int(quantity1)*float(price1) + int(quantity2)*float(price2))

print("VALOR A PAGAR: R$ %.2f" %total_price)

