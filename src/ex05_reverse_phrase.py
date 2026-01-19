"""
Ejercicio 5: escribir una frase y mostrarla invertida (carácter a carácter).
"""

def reverse_phrase(s: str) -> str:
    """Devuelve la frase invertida (carácter a carácter)."""
    return s[::-1]


if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    frase_invertida = reverse_phrase(frase)
    print("\nFrase invertida:", frase_invertida)