def calcular_prestamo_compuesto(C, i, n):
    capital_final = C * (1 + i) ** n
    return capital_final

C = float(input("Ingrese el capital inicial del préstamo (C): "))
i = float(input("Ingrese la tasa de interés mensual (en %): "))
n = int(input("Ingrese el número de meses (n): "))

valor_final = calcular_prestamo_compuesto(C, i, n)

print(f"\nEl valor final del préstamo es: ${valor_final:.2f}")