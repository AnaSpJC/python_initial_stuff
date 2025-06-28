def main():
    cadena = input("Cadena?: ")
    print("¿Qué función querés ejecutar?:\n F1 \n F2 \n F3 \n F4 \n F5")
    opcion = input("Esperando tu respuesta... ")
    if opcion == "F1" or opcion == "f1":
        f1(cadena)
    elif opcion == "F2" or opcion == "f2":
        f2(cadena)
    elif opcion == "F3" or opcion == "f3":
        f3(cadena)
    elif opcion == "F4" or opcion == "f4":
        f4(cadena)
    elif opcion == "F5" or opcion == "f5":
        f5(cadena)
    else:
        print("Elegiste una opción que no está en el menú")

def f1(cadena):
    print("Opción F1: ", "*".join(cadena))

def f2(cadena):
    print("Opción F2: ", end="")
    subcadena = input("Subcadena?: ")
    if cadena.startswith(subcadena) == True:
        print(f"Tu cadena empieza con {subcadena}")
    else:
        print(f"Tu cadena no empieza con la subcadena ingresada")       

def f3(cadena):
    print("Opción F3: ", end="") 
    caracter = input("Ingresá un caracter: ").lower()
    if caracter.isalnum() == False:
        print("El caracter debe ser alfanumérico!")
    else:
        count = 0
        for i in cadena:
            if i == caracter:
                count += 1 #count = count +1
        print(f"{caracter} aparece {count} veces en la cadena")

def f4(cadena):
    print("Opción F4: Contando las palabras...")
    # sacando espacios al principio y al final
    cadena_limpia = cadena.strip()
    # eliminando espacios vacíos entre palabras > 1(ej HOLA(espacio espacio)MUNDO)
    while "  " in cadena_limpia:
        cadena_limpia = cadena_limpia.replace("  ", " ")
    # contando los espacios dentro de la frase
    count = 0
    for i in cadena_limpia:
        if i == " ":
            count += 1
    if count != 0:
        print(f"La frase tiene {count + 1} palabras")
    else:
        print("Es sólo una palabra")

def f5(cadena):
    print("Opción F: Inviertiendo cadena e index múltiplo de 4...")
    print(f"Cadena invertida: \n{cadena[-1::-1]}")
    print("Los caracteres con índices múltiplos de 4 son:")
    print("***NOTA: Se incluye el '0' porque es múltiplo universal de números enteros***")
    for i in range(0, len(cadena)):
        if i % 4 == 0:
            print(cadena[i], end="")
    
    print()
main()      
