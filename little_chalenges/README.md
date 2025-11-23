# Conteo de Caracteres (Ejercicio)

![fcc Challenge](assets/Image%202025-11-23.jpeg)

Este programa toma una frase ingresada por el usuario, cuenta cuántas veces aparece cada letra del abecedario (ignorando espacios, números, mayúsculas y signos), y devuelve los resultados ordenados alfabéticamente.

A continuación se explica **paso a paso** cómo funciona la función que realiza el conteo y el ordenamiento.

---

## 🧠 ¿Qué hace la función `count_characters`?

1. **Convierte toda la frase a minúsculas.**  
   Esto simplifica el conteo, porque así `"A"` y `"a"` se consideran la misma letra.

2. **Recorre la frase carácter por carácter.**

3. **Filtra para quedarse solo con letras entre `'a'` y `'z'`.**  
   De esta manera se ignoran:
   - espacios  
   - números  
   - tildes  
   - símbolos  
   - signos de puntuación  

4. **Cuenta cuántas veces aparece cada letra** usando un diccionario de Python:

   ```python
   counts[char] = counts.get(char, 0) + 1

    Esto significa:

    - si la letra **no estaba**, `counts.get(char, 0)` devuelve `0`
    - si la letra **ya existía**, devuelve el número actual
    - luego se suma **1** para actualizar el conteo

5. **Ordena las letras alfabéticamente usando:**
*sorted(counts)*
6. **Devuelve una lista de strings con este formato:**
"a 3"
"b 1"
"c 2"

## Ideas para mejorar

- permitir elegir un separador personalizado  
- normalizar tildes (`á → a`, `é → e`, etc.)  
- devolver también un diccionario con los valores  
- comparar dos frases distintas  
- guardar o exportar los resultados  
