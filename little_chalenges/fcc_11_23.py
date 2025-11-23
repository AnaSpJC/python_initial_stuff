# 1) Función que cuenta caracteres
def count_characters(sentence):
    sentence = sentence.lower()
    counts = {}

    for char in sentence:
        if 'a' <= char <= 'z':
            counts[char] = counts.get(char, 0) + 1

    return [f"{letter} {counts[letter]}" for letter in sorted(counts)]


# 2) Pedir frase al usuario
sentence = input("Escribí una frase para analizar: ")

# 3) Ejecutar función y mostrar resultado
resultado = count_characters(sentence)

print("Resultado en una sola línea:")
print(" - ".join(resultado))     # Formato con guiones

print("\nLista (array) completa:")
print(resultado)                 # Mostrar la lista