def test_lucas_lehmer(p):
    """Verifica si 2^p - 1 es un número primo de Mersenne"""
    if p == 2: return True
    m_p = 2**p - 1
    s = 4
    for _ in range(p - 2):
        s = (s**2 - 2) % m_p
    return s == 0

def es_primo(n):
    """Función auxiliar para verificar si el exponente p es primo"""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def calcular_perfectos_pro(cantidad):
    encontrados = 0
    p = 2
    print(f"Buscando los primeros {cantidad} números perfectos...")
    
    while encontrados < cantidad:
        if es_primo(p):
            if test_lucas_lehmer(p):
                # Aplicamos la fórmula: 2^(p-1) * (2^p - 1)
                perfecto = (2**(p-1)) * (2**p - 1)
                encontrados += 1
                print(f"#{encontrados}: {perfecto} \n >> (Primo asociado = {p})")
        p += 1

# Ejecutar el buscador
calcular_perfectos_pro(20)