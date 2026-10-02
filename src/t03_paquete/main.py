"""Herramienta matemática interactiva."""

from t03_paquete import conversor, geometria, numeros


def mostrar_menu() -> None:
    print("\n=== Herramienta matemática ===")
    print("  1. Test de primalidad")
    print("  2. MCD de dos enteros")
    print("  3. Área de un círculo")
    print("  4. Conversión de temperatura (°C → °F)")
    print("  0. Salir")
    print("------------------------------")


def ejecutar() -> None:
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                n = int(input("n: "))
                print(f"{n} es primo: {numeros.es_primo(n)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                a = int(input("a: "))
                b = int(input("b: "))
                print(f"mcd({a}, {b}) = {numeros.mcd(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                r = float(input("Radio: "))
                print(f"Área = {geometria.area_circulo(r):.6f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                c = float(input("Temperatura en °C: "))
                print(f"{c} °C = {conversor.celsius_a_fahrenheit(c):.2f} °F")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "0":
            print("Hasta luego.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar()
