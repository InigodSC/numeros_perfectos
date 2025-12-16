from time import time
import csv
from datetime import datetime
import math
import sys

LOG10_2 = math.log10(2)

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

def _numero_de_digitos_por_bitlength(n):
    """Calcula el número de dígitos en base 10 usando bit_length (sin convertir a str)."""
    if n == 0:
        return 1
    # bit_length - 1 es el exponente del bit más alto
    return int((n.bit_length() - 1) * LOG10_2) + 1

def generar_perfectos_csv(cantidad, nombre_base_csv):
    """
    Genera `cantidad` números perfectos y los escribe en un CSV.

    Columnas del CSV:
      - posicion
      - numero: si es razonablemente pequeño se guarda el número decimal completo,
                si es muy grande se guarda la fórmula "2^(p-1)*(2^p-1)" para evitar conversiones pesadas.
      - primo_asociado: el exponente p
      - numero_de_digitos: número de dígitos en base 10 (calculado sin convertir a string)
      - tiempo_segundos: tiempo transcurrido desde inicio hasta generación de ese número
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

                    # calculamos el número de dígitos sin convertir a cadena
                    digits = _numero_de_digitos_por_bitlength(perfecto)

                    # Intentamos convertir a string sólo si es razonable; evitamos el ValueError de Python 3.11+
                    numero_a_guardar = None
                    try:
                        # Intentar conversión; puede lanzar ValueError si supera el límite
                        numero_a_guardar = str(perfecto)
                    except (ValueError, OverflowError):
                        # Fallback: guardamos la fórmula en vez del número decimal completo
                        numero_a_guardar = f"2^{p-1}*(2^{p}-1)"
                    except MemoryError:
                        numero_a_guardar = f"2^{p-1}*(2^{p}-1)"

                    writer.writerow([encontrados, numero_a_guardar, p, digits, elapsed])
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
