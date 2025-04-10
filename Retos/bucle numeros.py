numero=int(input("Digita un numero positivo: "))

while numero <= 0:
    print("Debe ingresar un número positivo.")
    numero = int(input("Digita un numero positivo: "))

if numero > 0:
    for i in range(1, numero + 1):
        print(i)