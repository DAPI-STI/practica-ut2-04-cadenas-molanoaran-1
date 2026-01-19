"""
Ejercicio 2: leer un nombre completo (nombre + apellidos) y mostrar:

Todo en minúsculas.

Todo en mayúsculas.

Capitalizado (primera letra de cada palabra en mayúscula).

La función devolverá una tupla: (minusculas, mayusculas, capitalizado).
"""

def name_variants(full_name: str) -> tuple[str, str, str]:
    """Devuelve (minusculas, MAYUSCULAS, Capitalizado-Por-Palabra)."""
    minusculas = full_name.lower()
    mayusculas = full_name.upper()
    capitalizado = full_name.title()
    return (minusculas, mayusculas, capitalizado)


if __name__ == "__main__":
    full_name = input("Ingresa tu nombre completo: ")

    minus, mayus, cap = name_variants(full_name)

    print("\nTodo en minúsculas:", minus)
    print("Todo en MAYÚSCULAS:", mayus)
    print("Capitalizado:", cap)