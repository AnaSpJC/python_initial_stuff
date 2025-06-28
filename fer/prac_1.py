#Escribir por pantalla cada carácter de la cadena recibida, en un mismo
#renglón separados por un guiones. 

var1 = "Tengo Frío"
var2 = "chocolate blanco"
var3 = 123

#Con iteración: (ojo caracter final)
for i in var1:
    #print(i)
    print(i, end="-")

# Con método JOIN(): join(con lo que quiero unir.join(cadena))
#       Usando variables
guiones = "-".join(var1)
print(guiones)
#       Usando el print directamente
print("-".join(var1))