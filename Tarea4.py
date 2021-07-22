



gastos = int
dinero = int

dinero = input("Dinero:")
gastos = input("Gastos:")
total = int(dinero) - int(gastos)
print(total)



if total < 0:
    print('Debes dinero,te vamos a partir las piernas')

elif total < 100:
    print("Eres pobre")
elif total == 0:
    print("Eres pobre")
elif total > 100:
    print("Estas pastao")




