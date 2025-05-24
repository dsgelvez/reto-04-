import math

def calcular_area(r, a, b):
    area_cuerpo = a * (b - 2*r) + math.pi * r**2
    area_ruedas = 2 * math.pi * r**2
    area_total = area_cuerpo + area_ruedas
    return area_total

def calcular_perimetro(r, a, b):
    perimetro = 2 * a + 2 * (b - 2*r) + 2 * math.pi * r
    return perimetro

r = float(input("Ingrese el radio de las ruedas y bordes (r): "))
a = float(input("Ingrese la altura del cuerpo rectangular (a): "))
b = float(input("Ingrese el largo total del cuerpo (b): "))

area = calcular_area(r, a, b)
perimetro = calcular_perimetro(r, a, b)

print(f"\nÁrea total: {area:.2f} unidades cuadradas")
print(f"Perímetro del cuerpo: {perimetro:.2f} unidades")