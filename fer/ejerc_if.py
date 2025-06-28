# Desarrollá un código en el que se informe si una persona está habilitada para tramitar
#el registro sin ningún requisito extra, según la edad. (Edad mínima 18, edad máxima 70 años)
edad=int(input("ingrese su edad: "))
if edad>18 and edad<70:
    print("no tiene ningun requisito extra")
elif edad<18:
    print("sos menor")
else:
    print("excediste la edad maxima")