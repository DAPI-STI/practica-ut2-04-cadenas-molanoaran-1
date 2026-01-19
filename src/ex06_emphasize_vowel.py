"""
Ejercicio 6: pedir una frase y una vocal y mostrar la frase con la vocal en mayúsculas.

La función debe:

Recibir una frase y una vocal (a, e, i, o, u) en cualquier caso.

Devolver la frase sustituyendo esa vocal (mayúscula/minúscula) por su versión en mayúscula.

Si la vocal no es válida, lanzar ValueError.
"""

def emphasize_vowel(phrase: str, vowel: str) -> str:
    """Convierte a mayúscula todas las apariciones de vowel (sin distinguir mayúsculas)."""
    vowel = vowel.lower().strip()

    if len(vowel) != 1 or vowel not in "aeiou":
        raise ValueError("Debes introducir una sola vocal válida: a, e, i, o, u.")

    return "".join(c.upper() if c.lower() == vowel else c for c in phrase)


if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    vocal = input("Elige una vocal a resaltar (a, e, i, o, u): ")

    try:
        resultado = emphasize_vowel(frase, vocal)
        print("\nFrase resultante:", resultado)
    except ValueError as e:
        print("Error:", e)