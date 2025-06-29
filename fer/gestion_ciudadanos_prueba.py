"""
import sqlite3
conexion = sqlite3.connect('BUENOS_AIRES.db')
cursor = conexion.cursor()

cursor.execute('''
            CREATE TABLE ciudadanos (
                DNI TEXT PRIMARY KEY,
                nombre_apellido TEXT NOT NULL,
                Barrio TEXT,
                Edad INTEGER
            )
        ''')
cursor.execute("INSERT INTO ciudadanos (DNI, nombre_apellido, Barrio, Edad) VALUES (?, ?, ?, ?)",
                       (dni, nombre_apellido, barrio, edad))
conexion.commit()

cursor.execute("SELECT DNI, nombre_apellido, Barrio, Edad FROM ciudadanos WHERE DNI = ?", (dni,))
cursor.fetchone()
        
cursor.execute("SELECT DNI, nombre_apellido, Barrio, Edad FROM ciudadanos ORDER BY DNI")
cursor.fetchall()

cursor.execute("DELETE FROM ciudadanos WHERE DNI = ?", (dni,))
conexion.commit()

conexion.close()

          """