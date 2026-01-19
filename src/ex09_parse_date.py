"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de 'dd/mm/aaaa'."""
    partes = date_str.strip().split("/")

    if len(partes) != 3:
        raise ValueError("Formato incorrecto. Usa 'dd/mm/aaaa'.")

    dia_str, mes_str, anio_str = partes

    if not (dia_str.isdigit() and mes_str.isdigit() and anio_str.isdigit()):
        raise ValueError("La fecha debe contener solo números.")

    dia, mes, anio = int(dia_str), int(mes_str), int(anio_str)

    if not (1 <= mes <= 12):
        raise ValueError("El mes debe estar entre 1 y 12.")
    if not (1 <= dia <= 31):
        raise ValueError("El día debe estar entre 1 y 31.")
    if anio < 1:
        raise ValueError("El año debe ser mayor que 0.")

    return (dia, mes, anio)


if __name__ == "__main__":
    fecha = input("Introduce una fecha (formato dd/mm/aaaa): ")
    try:
        dia, mes, anio = parse_date(fecha)
        print(f"\nDía: {dia}")
        print(f"Mes: {mes}")
        print(f"Año: {anio}")
    except ValueError as e:
        print("Error:", e)