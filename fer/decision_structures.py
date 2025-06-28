numero = int(input("Ingresá número positivo menor a 10: "))
"""par = numero % 2
if par == 0:
    print(par)
else:
    print(par, end="")
    print("  El num es impar")
"""
if 10> numero > 0:
    print(numero*1)
    print(numero*2)
    print(numero*3)
    print(numero*4)
    print(numero*5)
    print(numero*6)
    print(numero*7) 
elif numero < 0:
    print(f"El número {numero} es negativo!")
else:
    print(f"El número {numero} que ingresaste en más grande que el pedido!")
