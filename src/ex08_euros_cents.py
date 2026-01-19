"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    price_str = price_str.strip().replace(",", ".")
    partes = price_str.split(".")

    if len(partes) != 2 or len(partes[1]) != 2:
        raise ValueError("El precio debe tener dos decimales, por ejemplo '123.45'.")

    euros_part, cents_part = partes

    if not euros_part.isdigit() or not cents_part.isdigit():
        raise ValueError("El precio debe contener solo números y un separador decimal.")

    return (int(euros_part), int(cents_part))


if __name__ == "__main__":
    precio = input("Introduce un precio con dos decimales (por ejemplo 123.45 o 123,45): ")
    try:
        euros, centimos = euros_cents(precio)
        print(f"\nEuros: {euros}")
        print(f"Céntimos: {centimos}")
    except ValueError as e:
        print("Error:", e)