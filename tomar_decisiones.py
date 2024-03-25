import random

CANTIDAD_NUMEROS = 50_000
pares = 0
impares = 0

for i in range(0, CANTIDAD_NUMEROS):
    valor = random.randint(0, 100)
    if valor % 2 == 0:
        pares += 1
    else:
        impares +=1
    
print(f"En una muestra de {CANTIDAD_NUMEROS} encontramos pares {pares}, impares {impares}")