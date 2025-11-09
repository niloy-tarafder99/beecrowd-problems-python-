variables = input().split(" ")

a , b , c = variables

A = float(a)
B = float(b)
C = float(c)

TRIANGULO = 0.5*A*C
CIRCULO = 3.14159*(C**2)
TRAPEZIO = ((A+B)/2)*C
QUADRADO = B**2
RETANGULO = A*B

print("TRIANGULO: %.3f" %TRIANGULO)
print("CIRCULO: %.3f" %CIRCULO)
print("TRAPEZIO: %.3f" %TRAPEZIO)
print("QUADRADO: %.3f" %QUADRADO)
print("RETANGULO: %.3f" %RETANGULO)