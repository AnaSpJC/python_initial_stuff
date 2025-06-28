"""Método: startswith("subcadena", posicion_inicio, posicion_fin
Método: endswith("subcadena", posicion_inicio, posicion_fin)"""

var1 = "Hola"
var2 = "Hola que tal"
var3 = "hola que tal"
var4 = "Que tal"

#print(var2.startswith(var1))

if var1.startswith("Hola") == True:
    print("Yes")
else:
    print("Nop")

if var3.startswith("Hola".lower()) == True:
    print("Yes")
else:
    print("Nop")

if var4.startswith(var1) == True:
    print("Yes")
else:
    print("Nop")



