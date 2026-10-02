"""Módulo de conversión de unidades."""


def celsius_a_fahrenheit(c: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return 9 / 5 * c + 32


def fahrenheit_a_celsius(f: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return 5 / 9 * (f - 32)


def celsius_a_kelvin(c: float) -> float:
    """Convierte grados Celsius a Kelvin. Precondición: c >= -273.15."""
    if c < -273.15:
        raise ValueError(
            f"celsius_a_kelvin: temperatura por debajo del cero absoluto, recibido {c}"
        )
    return c + 273.15


def radianes_a_grados(r: float) -> float:
    """Convierte radianes a grados."""
    import math

    return r * 180 / math.pi


def grados_a_radianes(g: float) -> float:
    """Convierte grados a radianes."""
    import math

    return g * math.pi / 180


if __name__ == "__main__":
    print(f"100 °C en °F:  {celsius_a_fahrenheit(100):.2f}")
    print(f"212 °F en °C:  {fahrenheit_a_celsius(212):.2f}")
    print(f"0 °C en K:     {celsius_a_kelvin(0):.2f}")
    print(f"π rad en °:    {radianes_a_grados(3.141592653589793):.4f}")
    # prueba de precondición: temperatura bajo cero absoluto debe lanzar ValueError
    try:
        celsius_a_kelvin(-300)
    except ValueError as e:
        print(f"Error: {e}")
