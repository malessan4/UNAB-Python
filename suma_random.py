import random #importamos una libreria

suma = 0 

for j in range (0, 100):
    valor = random.random() * 10
    print(f"Pasada N# {j} número aleatorio generado {valor}")
    suma += valor
    
print(f"La suma de aleatorios es... {suma}")
    