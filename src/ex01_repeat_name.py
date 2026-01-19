"""
Ejercicio 1: pedir un nombre y un número entero e imprimir el nombre tantas veces
como indique el número.

Aquí lo hacemos como función:

Recibe un nombre (str) y un entero n.

Devuelve una cadena con el nombre repetido n veces, una por línea.

Si n <= 0, devolvemos cadena vacía.
"""

def repeat_name(name: str, n: int) -> str:
    """Devuelve el nombre repetido n veces, cada uno en una línea."""
    if n <= 0:
        return ""
    return "\n".join([name] * n)


if __name__ == "__main__":
    # --- Programa principal ---
    name = input("Ingresa tu nombre: ")
    n = int(input("Ingresa un número entero: "))
    print(repeat_name(name, n))