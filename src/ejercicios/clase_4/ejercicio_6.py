"""
Calcula el IMC (peso / (est ** 2))

Entradas:
El peso en kg
La estatura en metros

Salidas:
- Si peso menor a 18.5 => Bajo Peso
- Si peso mayor o igual a 18.5 y menor a 25 => "Normal"
- Si peso mayor o igual a 25 y menor a 30 => Sobrepeso
- Si peso mayor o igual a 30 => Obesidad

Ejemplo de ejecución:
>>> 1
>>> 2

IMC: 18.7 => Obesidad
"""
#Alexhia Sophia Pérez Escobar || A01825459


print ("\t<<--------  CALCULADORA DE IMC -------->>")
print ("¡Bienvenido!")
print ()

peso = float(input("Ingresa tu peso en kg: "))
est = float(input("Ingresa tu estatura en metros: "))


imc = peso / (est ** 2)


print (f"IMC: {imc:.1f}")

if imc < 18.5:
    print ("Bajo peso")

elif imc >= 18.5 and imc < 25:
    print ("Normal")

elif imc >= 25 and imc < 30:
    print ("Sobrepeso")
    
else:
    print ("Obesidad")

print ("\t<<---------- ¡Gracias! ---------->>")
