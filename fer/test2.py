def main():
    cant_alumnos = int(input("Cuántos alumnos hay en 5to año?: "))
    while cant_alumnos <= 0: 
        print("Ingresá un valor válido")
    
    lista_de_notas = obtener_notas(cant_alumnos)
    maxima = nota_maxima(lista_de_notas)
    print(f"La nota máxima es {maxima}")
    print(promedio(lista_de_notas))
    lista_asterisco = asterisco(lista_de_notas, maxima)
    for i in range(len(lista_asterisco)):
        print(f"Nota {i + 1}: {lista_asterisco[i]}")

def obtener_notas(cant):
    notas = []
    for i in range(cant):
        nota = float(input("Ingresá la nota: "))
        while  nota < 0 or nota > 10:
            nota = float(input("Nota no válida (debe ser entre 0 y 10. Ingresá de nuevo: "))
        notas.append(nota)
    return notas

def nota_maxima(lista):
    aux = 0
    for i in lista:
        if i >= aux:
            aux = i
    return aux

def promedio(lista): 
    suma = 0
    for i in lista:
        suma += i
    prom = suma / len(lista)
    return (f"El promedio es {prom}")

def asterisco(lista, max):

    for i in range(len(lista)):
        if lista[i] == max:
            lista[i] = "*"
    return lista



if __name__ == "__main__":
    main()