list=[]

op1=int(input("¿Cuántos integrantes son?\n 1.- Solo un integrante \n 2.- Dos o más \n\n Opción:  "))
if op1 == 1:
    nombre=input("Ingrese el nombre del integrante: ")
    list.append(nombre)
    print(list)
elif op1 == 2:
    cantidad=int(input("Ingrese la cantidad de integrantes: "))
    for i in range(cantidad):
        nombres=input("Ingrese los nombres de los integrantes: ")
        list.append(nombres)
    print(list)
else:
    print("Opción errónea")