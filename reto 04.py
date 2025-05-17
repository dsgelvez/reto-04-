# ===================================================
# Ejercicios básicos de condicionales en Python
# Autor: Santiago Gelvez Morales
# Descripción: Solución paso a paso reto 04
# ===================================================

# --------------------------------------
# PROBLEMA 1:
# Determinar si un número corresponde al código ASCII de una vocal minúscula
# --------------------------------------

def es_ascii_de_vocal_minuscula(numero):
    letra = chr(numero)  # Convertimos el número a letra
    if letra in 'aeiou':
        return True
    else:
        return False

print("Problema 1:", es_ascii_de_vocal_minuscula(97))  # True ('a')


# --------------------------------------
# PROBLEMA 2:
# Verificar si el código ASCII de un carácter es par o no
# --------------------------------------

def ascii_par_o_no(caracter):
    codigo = ord(caracter)  # Obtenemos el código ASCII
    if codigo % 2 == 0:
        return "El código ASCII es par"
    else:
        return "El código ASCII es impar"

print("Problema 2:", ascii_par_o_no("A"))


# --------------------------------------
# PROBLEMA 3:
# Verificar si un carácter es un dígito (0-9)
# --------------------------------------

def es_digito(caracter):
    if caracter.isdigit():
        return "Es un dígito"
    else:
        return "No es un dígito"

print("Problema 3:", es_digito("8"))


# --------------------------------------
# PROBLEMA 4:
# Verificar si un número es múltiplo de otro
# --------------------------------------

def es_multiplo(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero"
    if num1 % num2 == 0:
        return "Es múltiplo"
    else:
        return "No es múltiplo"

print("Problema 4:", es_multiplo(10, 2))


# --------------------------------------
# PROBLEMA 5:
# Clasificar un número real como positivo, negativo o cero
# --------------------------------------

def clasificar_numero(x):
    if x > 0:
        return f"El número {x} es positivo"
    elif x < 0:
        return f"El número {x} es negativo"
    else:
        return f"El número {x} es el neutro para la suma"

print("Problema 5:", clasificar_numero(0))


# --------------------------------------
# PROBLEMA 6:
# Verificar si un punto está dentro de un círculo
# --------------------------------------

def pertenece_al_circulo(centro, radio, punto):
    distancia_cuadrada = (punto[0] - centro[0])**2 + (punto[1] - centro[1])**2
    if distancia_cuadrada < radio**2:
        return "El punto está dentro del círculo"
    else:
        return "El punto NO está dentro del círculo"

print("Problema 6:", pertenece_al_circulo((0, 0), 5, (2, 2)))


# --------------------------------------
# PROBLEMA 7:
# Verificar si tres longitudes pueden formar un triángulo
# --------------------------------------

def es_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Sí se puede formar un triángulo"
    else:
        return "No se puede formar un triángulo"

print("Problema 7:", es_triangulo(3, 4, 5))


# --------------------------------------
# PROBLEMA 8:
# Devolver la capital de un país de América usando match-case
# --------------------------------------

def capital_americana(pais):
    match pais:
        case "colombia":
            return "Bogotá"
        case "argentina":
            return "Buenos Aires"
        case "perú":
            return "Lima"
        case "chile":
            return "Santiago"
        case "brasil":
            return "Brasilia"
        case "uruguay":
            return "Montevideo"
        case "ecuador":
            return "Quito"
        case "méxico":
            return "Ciudad de México"
        case "canadá":
            return "Ottawa"
        case "estados unidos":
            return "Washington, D.C."
        case _:
            return "País no identificado"

print("Problema 8:", capital_americana("perú"))
print("Problema 8:", capital_americana("españa"))
