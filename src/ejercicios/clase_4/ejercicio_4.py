"""
Escribe un programa que pida un número al usuario.
Si el número es menor a 0 deberá imprimir negativo
Si es igual a 0 deberá imprimir cero
Si es mayor a 0 deberá imprimir positivo
"""
#Alexhia Sophia Pérez Escobar || A01825459

# Escribe un programa que pida un número al usuario. 
# Si el número es menor a 0 deberá imprimir negativo
# Si es igual a 0 deberá imprimir cero
# Si es mayor a 0 deberá imprimir positivo

print("\t<<-----  NEGATIVO O POSITIVO----->>")
print("¡Bienvenido!")
print()
num = float (input("Por favor, ingresa un número: "))

print()

if num==0:
         print("Cero")
elif(num>0):
    print("Positivo")
else:
    print("Negativo")

print("\t<<---------- ¡Gracias! ---------->>")

