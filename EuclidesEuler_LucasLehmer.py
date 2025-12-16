from time import time
import csv
from datetime import datetime

def test_lucas_lehmer(p):
    """Verifica si 2^p - 1 es un número primo de Mersenne"""
    if p == 2:
        return True
    m_p = 2**p - 1
    s = 4
    for _ in range(p - 2):
        s = (s**2 - 2) % m_p
    return s == 0

def es_primo(n):
    """Función auxiliar para verificar si el exponente p es primo"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(n**0.5) + 1
    for i in range(3, r, 2):
        if n % i == 0:
            return False
    return True

def generar_perfectos_csv(cantidad, nombre_base_csv):
    """Genera `cantidad` números perfectos y los escribe en un CSV.

    El CSV contiene: posicion, numero, primo_asociado, numero_de_digitos, tiempo_segundos
    donde tiempo_segundos es el tiempo desde el inicio del proceso hasta que se generó ese número.
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{nombre_base_csv}_{timestamp}.csv"

    start_time = time()
    encontrados = 0
    p = 2

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['posicion', 'numero', 'primo_asociado', 'numero_de_digitos', 'tiempo_segundos'])

        print(f"Generando los primeros {cantidad} números perfectos y guardando en '{filename}'...")

        while encontrados < cantidad:
            if es_primo(p):
                if test_lucas_lehmer(p):
                    perfecto = (2**(p-1)) * (2**p - 1)
                    encontrados += 1
                    elapsed = round(time() - start_time, 6)
                    digits = len(str(perfecto))
                    # Escribimos el número como cadena para evitar problemas de formato
                    writer.writerow([encontrados, str(perfecto), p, digits, elapsed])
                    print(f"  -> #{encontrados} generado (p={p}, digitos={digits}, tiempo={elapsed}s)")
            p += 1

    print(f"Proceso completado. Archivo guardado: {filename}")
    return filename


if __name__ == '__main__':
    try:
        while True:
            raw = input("¿Cuántos números perfectos quieres generar? ").strip()
            if not raw:
                print("Introduce un número entero positivo.")
                continue
            try:
                cantidad = int(raw)
                if cantidad <= 0:
                    print("Introduce un número entero positivo mayor que 0.")
                    continue
                break
            except ValueError:
                print("Entrada no válida. Introduce un número entero.")

        nombre_base = input("Nombre base para el CSV (sin extensión, por ejemplo 'resultados'): ").strip()
        if not nombre_base:
            nombre_base = 'resultados'

        generar_perfectos_csv(cantidad, nombre_base)

    except KeyboardInterrupt:
        print('\nInterrumpido por el usuario. No se han completado todas las operaciones.')
