import random

def lanzar_dado():
    return random.randint(1, 6)

def simulacion_lanzamientos(cantidad_lanzamientos):
    resultados = []
    for _ in range(cantidad_lanzamientos):
        resultado = lanzar_dado()
        resultados.append(resultado)
    return resultados

cantidad_lanzamientos = int(input("¿Cuántas veces deseas lanzar el dado? "))
resultados = simulacion_lanzamientos(cantidad_lanzamientos)
print("Resultados de los lanzamientos:", resultados)