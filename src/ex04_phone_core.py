"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Devuelve la parte central del teléfono, validando formato +XX-YYYYYYY-ZZ.
    """
    s = s.strip()
    partes = s.split("-")

    if len(partes) != 3:
        raise ValueError("El número debe tener tres partes separadas por '-'.")

    prefijo, central, sufijo = partes

    if not prefijo.startswith("+"):
        raise ValueError("El prefijo debe comenzar con '+'.")

    if not central.isdigit():
        raise ValueError("La parte central debe ser numérica.")

    return central


if __name__ == "__main__":
    telefono = input("Ingresa un número de teléfono con formato +XX-YYYYYYY-ZZ: ")
    try:
        core = phone_core(telefono)
        print("Parte central del número:", core)
    except ValueError as e:
        print("Error:", e)