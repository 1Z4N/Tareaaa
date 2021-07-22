#Pedir un numero a un usuario y decir si un numero es par o no

edad = input("Edad:")

edad = int(edad)

if edad % 2 == 0:
    print("Par")

else:
    print('Impar')