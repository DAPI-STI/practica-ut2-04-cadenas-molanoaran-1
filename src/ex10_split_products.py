"""
Ejercicio 10: leer una lista de productos separados por comas y mostrar cada uno en una línea.

La función:

Recibe una cadena tipo "pan, leche, huevos".

Devuelve una lista con ["pan", "leche", "huevos"], sin espacios sobrantes.
"""

def split_products(csv_line: str) -> list[str]:
    """Devuelve una lista de productos sin espacios extra a partir de una línea CSV simple."""
    return [p.strip() for p in csv_line.split(",") if p.strip()]


if __name__ == "__main__":
    linea = input("Escribe una lista de productos separados por comas: ")
    productos = split_products(linea)

    print("\nProductos:")
    for p in productos:
        print("-", p)