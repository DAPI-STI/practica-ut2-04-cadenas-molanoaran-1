"""
Ejercicio 7: dado un correo electrónico, cambiar su dominio por "ceu.es".

La función:

Mantiene la parte local (antes de la arroba).

Sustituye el dominio por el indicado (por defecto "ceu.es").

Si el correo no tiene exactamente una arroba, lanza ValueError.
"""

def replace_domain(email: str, new_domain: str = "ceu.es") -> str:
    """Devuelve el correo con el dominio sustituido por new_domain."""
    email = email.strip()
    partes = email.split("@")

    if len(partes) != 2:
        raise ValueError("El correo debe tener exactamente una '@'.")

    local, dominio = partes
    return f"{local}@{new_domain}"


if __name__ == "__main__":
    correo = input("Ingresa tu correo electrónico: ")
    try:
        nuevo = replace_domain(correo)
        print("\nCorreo con dominio actualizado:", nuevo)
    except ValueError as e:
        print("Error:", e)