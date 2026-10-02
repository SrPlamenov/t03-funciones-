"""Módulo de funciones geométricas básicas."""

import math


def area_circulo(r: float) -> float:
    """Área de un círculo de radio r. Precondición: r >= 0."""
    if r < 0:
        raise ValueError(f"area_circulo: el radio debe ser no negativo, recibido {r}")
    return math.pi * r**2


def hipotenusa(a: float, b: float) -> float:
    """Longitud de la hipotenusa dado los catetos a y b."""
    if a <= 0 or b <= 0:
        raise ValueError(
            f"hipotenusa: los catetos deben ser positivos, recibido a={a}, b={b}"
        )
    return math.sqrt(a**2 + b**2)


def es_triangulo_valido(a: float, b: float, c: float) -> bool:
    """True si a, b, c satisfacen la desigualdad triangular."""
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a


if __name__ == "__main__":
    print(f"Área círculo r=1:    {area_circulo(1):.6f}")
    print(f"Hipotenusa 3, 4:     {hipotenusa(3, 4):.6f}")
    print(f"Triángulo 3, 4, 5:   {es_triangulo_valido(3, 4, 5)}")
    print(f"Triángulo 1, 2, 10:  {es_triangulo_valido(1, 2, 10)}")
    # prueba de precondición: radio negativo debe lanzar ValueError
    try:
        area_circulo(-1)
    except ValueError as e:
        print(f"Error: {e}")
    # prueba de precondición: cateto no positivo debe lanzar ValueError
    try:
        hipotenusa(-3, 4)
    except ValueError as e:
        print(f"Error: {e}")
