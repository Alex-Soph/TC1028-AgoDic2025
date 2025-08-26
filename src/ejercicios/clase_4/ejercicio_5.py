"""
Crea un programa que pregunte al usuario un mes (1-12) y que imprima
la estación correspondiente.

Recuerda que:
Invierno (1, 2 y 12)
Primavera (3, 4 y 5)
Verano (6, 7, 8)
Otoño (9, 10, 11)
"""
#Alexhia Sophia Pérez Escobar || A01825459

# Crea un programa que pregunte al usuario un mes (1-12) y que imprima la estación correspondiente.

# Recuerda que: 
# Invierno (1, 2 y 12)
# Primavera (3, 4 y 5)
# Verano (6, 7, 8)
# Otoño (9, 10, 11)

print ("\t<<------------  MES ------------>>")
print ("¡Bienvenido!")
print ()
num = float (input("Por favor, ingresa un mes (1 - 12): "))

print()

if num == 1 or num == 2 or num == 12:
         print ("Invierno")

elif num == 3 or num == 4 or num== 5:
    print ("Primevera")

elif num == 6 or num == 7 or num == 8:
    print ("Verano")

elif num == 9 or num == 10 or num == 11:
    print ("Otoño")

else:
     print ("Ingrese un número válido (1 -12)")

print ("\t<<---------- ¡Gracias! ---------->>")

