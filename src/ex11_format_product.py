"""
Ejercicio 11: formatear información de un producto (nombre, precio, unidades).

La función:

Recibe nombre (str), precio (float) y unidades (int).

Devuelve una cadena formateada con:
nombre
precio unitario con 6 dígitos enteros y 2 decimales
unidades con 3 dígitos (relleno con ceros)
coste total (precio * unidades) con 8 enteros y 2 decimales
"""

def format_product(name: str, price: float, units: int) -> str:
    """Devuelve una descripción de producto formateada en una sola línea."""
    total = price * units
    # nombre con 10 col. (izquierda), luego 6 espacios antes de precio, 7 antes de total
    return f"{name:<10}      {price:>4.2f}       {total:>5.2f}"