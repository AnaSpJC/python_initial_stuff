#: Verifica si la cadena recibida comienza por una subcadena introducida por teclado
#: Verifica si la cadena recibida termina por una subcadena introducida por teclado
cadena=input("ingrese una cadena: ")
subcadena=input("ingrese una subcadena: ")
if cadena.startswith(subcadena.lower()):
    print("la cadena empieza con",subcadena)
else:
    print("la candena NO empieza con",subcadena)
if cadena.endswith(subcadena.lower()):
    print("la cadena termina con",subcadena)
else:
    print("la cadena NO termina con",subcadena)