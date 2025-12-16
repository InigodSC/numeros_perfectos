# Numeros Perfectos

Repositorio con implementaciones en Python para explorar y comprobar números perfectos y primos de Mersenne. Incluye un enfoque de fuerza bruta y una implementación basada en el teorema de Euclides–Euler junto con la prueba de Lucas–Lehmer para primos de Mersenne.

## Contenido
- [EuclidesEuler_LucasLehmer.py](https://github.com/InigodSC/numeros_perfectos/blob/main/EuclidesEuler_LucasLehmer.py) — Implementación del enfoque basado en el teorema de Euclides–Euler y la prueba de Lucas–Lehmer para comprobar si 2^p − 1 es primo y generar números perfectos pares a partir de primos de Mersenne.
- [fuerza_bruta.py](https://github.com/InigodSC/numeros_perfectos/blob/main/fuerza_bruta.py) — Búsqueda / comprobación de números perfectos mediante un método de fuerza bruta (suma de divisores).
- [README.md](https://github.com/InigodSC/numeros_perfectos/blob/main/README.md) — Este archivo.

## Requisitos
- Python 3.8+ (probablemente funciona en versiones posteriores).
- No deberían ser necesarias librerías externas; si algún script las requiere, se indicará en la cabecera del propio fichero.

## Uso básico
Abre una terminal y ejecuta los scripts con Python. Ejemplos genéricos:

- Ejecutar la comprobación por fuerza bruta:
```bash
python3 fuerza_bruta.py
```

- Ejecutar la versión basada en Euclides–Euler / Lucas–Lehmer:
```bash
python3 EuclidesEuler_LucasLehmer.py
```

Nota: Los parámetros concretos (por ejemplo, límite de búsqueda, valor de p para Lucas–Lehmer, etc.) dependen de cómo estén implementados los scripts. Puedes:
- Abrir los archivos para ver argumentos/funciones disponibles.
- Ejecutar `python3 script.py -h` o revisar los comentarios en el código para obtener instrucciones específicas si se ha programado manejo de argumentos.

## Explicación rápida de los métodos incluidos

- Teorema de Euclides–Euler (números perfectos pares):
  - Un número par N es perfecto si y sólo si N = 2^(p−1) * (2^p − 1) donde (2^p − 1) es primo (un primo de Mersenne).
  - Por tanto, buscar números perfectos pares se reduce a buscar primos de Mersenne.

- Prueba de Lucas–Lehmer (para primos de Mersenne M_p = 2^p − 1, p primo):
  - Define la sucesión: s_0 = 4, s_{n+1} = s_n^2 − 2 (mod M_p).
  - M_p es primo si y solo si s_{p−2} ≡ 0 (mod M_p).
  - Esta prueba es eficiente y el método recomendado para comprobar primos de Mersenne en rangos grandes.

- Fuerza bruta:
  - Consiste en calcular la suma propia de divisores (excluyendo el número) y comparar con el número. Es conceptualmente simple pero crece rápido en coste y sólo es práctico para números pequeños.

## Ejemplos
- Si el script `EuclidesEuler_LucasLehmer.py` acepta un parámetro `p`, un ejemplo típico sería:
```bash
python3 EuclidesEuler_LucasLehmer.py 7
```
(esto comprobaría si 2^7 − 1 = 127 es primo y, si lo es, reportaría el número perfecto asociado 2^(7−1) * 127 = 8128).

- Para `fuerza_bruta.py`, ejecutar sin argumentos podría listar números perfectos pequeños detectados en un rango predefinido por el script.

(Revisa los scripts para confirmar los nombres y formatos de los argumentos.)

## Testing / Validación
- Para valores pequeños puedes contrastar resultados con listas conocidas de números perfectos: 6, 28, 496, 8128, ...
- Para probar la prueba de Lucas–Lehmer, usa p = 2, 3, 5, 7, 13, ... donde algunos 2^p−1 son primos de Mersenne conocidos.
