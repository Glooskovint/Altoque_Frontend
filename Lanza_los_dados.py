import random
import time
import os

# Lanzar un dado
resultado = random.randint(1, 6)
os.system('cls')
print("La suerte a sido hechada")

# Mostrar barra de progreso
for i in range(101):
    porcentaje = i
    num_hashes = porcentaje // 2
    barra = '[' + '#' * num_hashes + '-' * (50 - num_hashes) + ']'
    print(f'\r{barra} {porcentaje}%', end='')
    time.sleep(0.05)

print(f"\nResultado del lanzamiento: {resultado}")