import sqlite3

def conectar_db():
    """Establece la conexión con la base de datos y crea la tabla si no existe."""
    try:
        conexion = sqlite3.connect('BUENOS_AIRES.db')
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ciudadanos (
                DNI TEXT PRIMARY KEY,
                nombre_apellido TEXT NOT NULL,
                Barrio TEXT,
                Edad INTEGER
            )
        ''')
        conexion.commit()
        print("Base de datos y tabla 'ciudadanos' listas.")
        return conexion, cursor
    except sqlite3.Error as e:
        print(f"Error al conectar o crear la tabla: {e}")
        return None, None

def ingresar_datos(cursor, conexion):
    """Permite al usuario ingresar datos de un nuevo ciudadano."""
    print("\n--- Ingresar Nuevos Ciudadanos ---")
    dni = input("DNI: ")
    nombre_apellido = input("Nombre y Apellido: ")
    barrio = input("Barrio: ")
    edad = input("Edad: ") # Leer como string para validar
    
    # Validación de Edad
    if not edad.isdigit():
        print("Error: La edad debe ser un número entero.")
        return
    edad = int(edad)

    try:
        cursor.execute("INSERT INTO ciudadanos (DNI, nombre_apellido, Barrio, Edad) VALUES (?, ?, ?, ?)",
                       (dni, nombre_apellido, barrio, edad))
        conexion.commit()
        print(f"Ciudadano '{nombre_apellido}' ingresado con éxito.")
    except sqlite3.IntegrityError:
        print("Error: Ya existe un ciudadano con ese DNI.")
    except sqlite3.Error as e:
        print(f"Error al ingresar datos: {e}")

def leer_dato_por_dni(cursor):
    """Busca y muestra un ciudadano por su DNI."""
    print("\n--- Buscar Ciudadano por DNI ---")
    dni = input("Ingrese el DNI del ciudadano a buscar: ")
    cursor.execute("SELECT DNI, nombre_apellido, Barrio, Edad FROM ciudadanos WHERE DNI = ?", (dni,))
    resultado = cursor.fetchone()
    if resultado:
        print("\n--- Datos del Ciudadano ---")
        print(f"DNI: {resultado[0]}")
        print(f"Nombre y Apellido: {resultado[1]}")
        print(f"Barrio: {resultado[2]}")
        print(f"Edad: {resultado[3]}")
    else:
        print("No se encontró ningún ciudadano con ese DNI.")

def mostrar_todos_los_datos(cursor):
    """Muestra todo el contenido de la tabla de ciudadanos de forma simple."""
    print("\n--- Listado Completo de Ciudadanos (Simple) ---")
    cursor.execute("SELECT DNI, nombre_apellido, Barrio, Edad FROM ciudadanos ORDER BY DNI")
    filas = cursor.fetchall()
    if filas:
        for fila in filas:
            print(fila) # Imprime cada fila como una tupla
    else:
        print("La tabla de ciudadanos está vacía.")

def borrar_dato_por_dni(cursor, conexion):
    """Borra un ciudadano de la tabla según su DNI."""
    print("\n--- Borrar Ciudadano por DNI ---")
    dni = input("Ingrese el DNI del ciudadano a borrar: ")
    try:
        cursor.execute("DELETE FROM ciudadanos WHERE DNI = ?", (dni,))
        if cursor.rowcount > 0:
            conexion.commit()
            print(f"Ciudadano con DNI {dni} borrado con éxito.")
        else:
            print("No se encontró ningún ciudadano con ese DNI.")
    except sqlite3.Error as e:
        print(f"Error al borrar datos: {e}")

def main():
    """Función principal que ejecuta el menú interactivo."""
    conexion, cursor = conectar_db()
    if conexion is None:
        print("No se pudo iniciar el programa debido a un error de conexión.")
        return

    while True:
        print("\n--- Menú de Gestión de Ciudadanos ---")
        print("1. Ingresar datos a la tabla")
        print("2. Leer un dato por DNI")
        print("3. Mostrar todo el contenido de la tabla")
        print("4. Borrar un dato por DNI")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingresar_datos(cursor, conexion)
        elif opcion == '2':
            leer_dato_por_dni(cursor)
        elif opcion == '3':
            mostrar_todos_los_datos(cursor)
        elif opcion == '4':
            borrar_dato_por_dni(cursor, conexion)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    # Asegurarse de cerrar la conexión al finalizar el programa
    if conexion:
        conexion.close()
        print("Conexión a la base de datos cerrada.")

# Esto asegura que main() se ejecute solo cuando el script es corrido directamente
if __name__ == "__main__":
    main()