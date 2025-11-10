t = int(input())
v = int(input())

s = v*t

fuel = s/12

#no need to convert this variable to float, this line of code is extra and for learning perpouse
fuel = float(fuel)

print("%.3f" %fuel)