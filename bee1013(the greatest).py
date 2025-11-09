variables = input().split(" ")

a, b, c = variables

A = int(a)
B = int(b)
C = int(c)

#greatest among A&B
g1 = (A+B+ abs(A-B))/2

#greatest among g1&c
g2 = (g1+C+ abs(g1-C))/2

print("%d eh o maior" %g2)
