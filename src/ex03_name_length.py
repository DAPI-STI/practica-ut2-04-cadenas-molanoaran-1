"""
Ejercicio 3: leer un nombre y mostrarlo en mayúsculas y cuántas letras tiene.

La función devolverá una tupla:
(nombre_en_mayusculas, numero_de_letras_sin_espacios)
"""

def name_upper_and_length(name: str) -> tuple[str, int]:
    """Devuelve (NAME_EN_MAYUSCULAS, numero_de_letras_sin_espacios)."""
    name_upper = name.upper()
    sin_espacios = len(name.replace(" ", ""))
    return (name_upper, sin_espacios)


if __name__ == "__main__":
    name = input("Ingresa tu nombre: ")
    name_upper, num_letras = name_upper_and_length(name)
    print("\nNombre en MAYÚSCULAS:", name_upper)
    print("Número de letras (sin contar espacios):", num_letras)