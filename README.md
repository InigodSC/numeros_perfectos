# Números Perfectos

Este repositorio explora los números perfectos: qué son, cómo se encuentran y dos enfoques de implementación en Python (fuerza bruta y Euclides–Euler + Lucas–Lehmer). El README explica la teoría básica y da indicaciones de uso de los scripts incluidos.

## ¿Qué es un número perfecto?

Un número natural N se llama perfecto si es igual a la suma de sus divisores propios (todos los divisores positivos distintos de N).  
Ejemplos pequeños bien conocidos:
- 6 = 1 + 2 + 3
- 28 = 1 + 2 + 4 + 7 + 14
- 496, 8128, ...

Los números perfectos pares están estrechamente relacionados con los primos de Mersenne (primos de la forma M_p = 2^p − 1 con p primo). No se conocen números perfectos impares (es un problema abierto si existen).

## Teorema de Euclides–Euler (números perfectos pares)

Euclides y Euler demostraron la condición necesaria y suficiente que relaciona primos de Mersenne y números perfectos pares:

- Si M_p = 2^p − 1 es primo (con p primo), entonces
  N = 2^(p−1) * (2^p − 1)
  es un número perfecto par.

- Además, todo número perfecto par puede expresarse de esa forma para algún primo p tal que 2^p − 1 sea primo.

Por tanto, la búsqueda de números perfectos pares se reduce a la búsqueda de primos de Mersenne.

## Prueba de Lucas–Lehmer (comprobar primos de Mersenne)

La prueba de Lucas–Lehmer es la prueba estándar y eficiente para verificar si M_p = 2^p − 1 es primo cuando p es primo:

1. Definir s_0 = 4.
2. Para n ≥ 0, s_{n+1} = s_n^2 − 2 (todo módulo M_p).
3. M_p es primo si y sólo si s_{p−2} ≡ 0 (mod M_p).

Esta prueba es mucho más rápida que hacer test de primalidad directo sobre M_p en la mayoría de casos prácticos.

## Métodos implementados en este repositorio

- [fuerza_bruta.py](https://github.com/InigodSC/numeros_perfectos/blob/main/fuerza_bruta.py)  
  Método directo: para cada número n calcula la suma de sus divisores propios y compara con n. Es simple pero crece rápidamente en coste y solo es práctico para números pequeños.

- [EuclidesEuler_LucasLehmer.py](https://github.com/InigodSC/numeros_perfectos/blob/main/EuclidesEuler_LucasLehmer.py)  
  Implementa:
  - Comprobación de primalidad del exponente p (simple).
  - Prueba de Lucas–Lehmer para verificar si 2^p − 1 es primo.
  - Generación de números perfectos pares mediante la fórmula de Euclides–Euler.
  - (Versión modificada) solicita cuántos números generar, pide un nombre base para un CSV y guarda los resultados en `<nombre>_YYYYMMDD_HHMMSS.csv` con las columnas:
    - posicion: índice (1, 2, 3, ...)
    - numero: el número perfecto (como cadena)
    - primo_asociado: el exponente p que produce el primo de Mersenne
    - numero_de_digitos: número de dígitos de N
    - tiempo_segundos: tiempo transcurrido desde el inicio del proceso hasta la generación de ese número

## Ejecución (uso básico)

Requisitos:
- Python 3.8+ (probado en versiones recientes).
- No se requieren librerías externas para las versiones incluidas.

Ejemplos:

- Ejecutar fuerza bruta:
```bash
python3 fuerza_bruta.py
```

- Ejecutar Euclides–Euler + Lucas–Lehmer (versión interactiva que genera CSV):
```bash
python3 EuclidesEuler_LucasLehmer.py
# El script preguntará cuántos números generar y el nombre base del CSV.
```

Salida: el script generará un archivo CSV en el directorio de ejecución con el nombre proporcionado más la fecha/hora.

Advertencias:
- Los números perfectos crecen muy rápido; calcular muchos de ellos requiere exponentes p grandes y un coste de cómputo y memoria elevado.
- La prueba de Lucas–Lehmer trabaja con enteros muy grandes (2^p − 1) y puede consumir tiempo y memoria si p es grande.

## Ejemplo teórico

Para p = 7:
- M_7 = 2^7 − 1 = 127 (es primo).
- Número perfecto: 2^(7−1) * (2^7 − 1) = 2^6 * 127 = 64 * 127 = 8128.

Tu script basado en Lucas–Lehmer detectará p = 7 como generador del cuarto número perfecto (8128) y lo guardará en el CSV con su tiempo de generación y número de dígitos.
