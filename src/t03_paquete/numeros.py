# numeros.py
"""Módulo con funciones básicas de teoría de números."""

import math


def es_primo(n: int) -> bool:
    """Devuelve True si n es primo (n debe ser >= 2)."""
    if n < 2:
        return False
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def mcd(a: int, b: int) -> int:
    """Máximo común divisor de a y b (algoritmo de Euclides)."""
    if b == 0:
        return a
    return mcd(b, a % b)


def mcm(a: int, b: int) -> int:
    """Mínimo común múltiplo de a y b."""
    return abs(a * b) // mcd(a, b)


def factorial(n: int) -> int:
    """Factorial de n. Precondición: n >= 0."""
    if n < 0:
        raise ValueError(f"factorial: no está definido para negativos, recibido {n}")
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Solo se ejecuta al lanzar: python numeros.py
    print("=== Pruebas del módulo numeros ===")
    print(f"es_primo(17)  = {es_primo(17)}")  # True
    print(f"es_primo(18)  = {es_primo(18)}")  # False
    print(f"mcd(48, 18)   = {mcd(48, 18)}")  # 6
    print(f"mcm(4, 6)     = {mcm(4, 6)}")  # 12
    print(f"factorial(10) = {factorial(10)}")  # 3628800
    # prueba de precondición: factorial(-1) debe lanzar ValueError
    try:
        factorial(-1)
    except ValueError as e:
        print(f"Error: {e}")
