invitados=[]
cantidad=int(input("Cuantos invitados tiene tu fiesta?: "))

for i in range(0,cantidad):
    invitado=input("Nombre de invitado: ")
    invitados.append(invitado)


respuesta = input("¿Deseas agregar más invitados? (si/no): ").lower()

while respuesta == "si":
    invitado = input("Nombre de invitado: ")
    invitados.append(invitado)
    respuesta = input("¿Deseas agregar más invitados? (si/no): ").lower()

invitados.sort()

for indice, i in enumerate(invitados):
    print("Invitado #"+str(indice+1)+": "+i.upper())



print("\nLista de invitados completa!")
input("\nPresiona Enter para salir...")
