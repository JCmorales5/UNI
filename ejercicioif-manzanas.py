print("\n*******************************************************")
print("            Comparando precios es las tiendas            ")
print("\n*******************************************************")

V1 = int(input("Ingrese el precio de la manzana del AMPM:  "))
V2 = int(input("Ingrese el precio de la manzana del SuperExpress:  "))

if V1 < V2:
    print(" Es menor el precio en AMPM")
if V2 < V1:
    print(" Es menor el precio en SuperExpress")
if V1 > V2:
    print(" Es mayor el precio en AMPM")
if V2 > V1:
    print(" Es mayor el precio en SuperExpress")
if V1 == V2:
    print(" Son iguales en ambas tiendas")
print("*******************************************************\n")