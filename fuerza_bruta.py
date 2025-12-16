def es_perfecto(n):
    suma_divisores = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

#print("Buscando números perfectos (Método manual)...")
#for num in range(2, 10000):
num = 0
while True:
    if es_perfecto(num):
        print(f"¡Encontrado!: {num}")
    num += 1