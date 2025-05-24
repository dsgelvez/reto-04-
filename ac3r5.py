def calcular_carne_aves(n_gallinas, m_gallos, k_pollitos):
    peso_total = (n_gallinas * 6) + (m_gallos * 7) + (k_pollitos * 1)
    return peso_total

n = int(input("Ingrese la cantidad de gallinas: "))
m = int(input("Ingrese la cantidad de gallos: "))
k = int(input("Ingrese la cantidad de pollitos: "))

peso_total = calcular_carne_aves(n, m, k)

print(f"\nCantidad total de carne de aves: {peso_total} kg"