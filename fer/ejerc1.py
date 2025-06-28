"""Diseñá un programa que indique si un número entero ingresado, es neutro y par, es
positivo y par, es positivo e impar, es negativo y par o es negativo e impar.
Ejemplos:
12 es positivo y par
-4 es negativo y par
0 es neutro y par
3 es positivo e impar
-45 es negativo e impar"""
numero=int(input("ingrese un numero: "))
resto=numero%2
if resto==0 and numero>0:
    print(numero," es par y positivo")
elif resto==0 and numero<0:
    print(numero," es par y negativo")
elif resto!=0 and numero>0:
    print(numero," es impar y positivo")
elif resto!=0 and numero<0:
    print(numero," es impar y negativo")
else:
    print(numero," es neutro y par")