from math import sqrt
print("Calculadora de Ecuaciones Cuadráticas")
A = float(input("Ingrese el valor de A: \n"))
B = float(input("Ingrese el valor B: \n"))
C = float(input("Ingrese el valor C: \n"))

def cuadratica(a, b, c):
	d = b**2 - 4*a*c
	if d < 0:
		return print(f"La respuesta es -{b} +- √{d*-1}i/{2*a}")
	elif sqrt(d) != int:
		resultado1 = f"-{b} + √{d}/{2*a}"
		resultado2 = f"-{b} - √{d}/{2*a}"
		return print(f"X1 = {resultado1} y X2 = {resultado2}")
	else:
		resultado1 = (-b + sqrt(d))/2*a
		resultado2 = (-b - sqrt(d))/2*a
		return print(f"X1 = {resultado1} y X2 = {resultado2}")
		
cuadratica(A,B,C)