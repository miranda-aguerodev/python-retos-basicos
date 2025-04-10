nombres = []
cantidad = int(input("Cuantos nombres deseas ingresar: "))

for i in range(0, cantidad):
    nombre = input("Digite el nombre: ")
    nombres.append(nombre)

nombres.sort()

for indice, nombre in enumerate(nombres):
    print(f"Nombre {indice + 1}: {nombre.upper()}")
