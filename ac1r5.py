import math

def calcular_volumen(r1, r2, h):
    volumen_hemisferio = (2/3) * math.pi * r1**3
    volumen_cono = (1/3) * math.pi * r2**2 * h
    volumen_total = volumen_hemisferio + volumen_cono
    return volumen_total

def calcular_area_superficial(r1, r2, h):
    area_hemisferio = 2 * math.pi * r1**2
    generatriz = math.sqrt(r2*2 + h*2)
    area_cono = math.pi * r2 * generatriz
    area_total = area_hemisferio + area_cono
    return area_total

r1 = float(input("Ingrese el radio del hemisferio (r1): "))
r2 = float(input("Ingrese el radio de la base del cono (r2): "))
h = float(input("Ingrese la altura del cono (h): "))

volumen = calcular_volumen(r1, r2, h)
area = calcular_area_superficial(r1, r2, h)

print(f"\nVolumen total: {volumen:.2f} unidades cúbicas")
print(f"Área superficial total: {area:.2f} unidades cuadradas")