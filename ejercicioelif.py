print("\n*******************************************************")
print("                       CALIFICACIONES                    ")
print("\n*******************************************************")
Nom1 = str(input( "Ingrese el Nombre del estudiante1: "))
print(" Hola", Nom1)
Nota1 = int(input("Agrega tu nota porfavor: "))

Nom2 = str(input( "Ingrese el Nombre del estudiante2: "))
print(" Hola", Nom2)
Nota2 = int(input("Agrega tu nota porfavor: "))

Nom3 = str(input( "Ingrese el Nombre del estudiante3: "))
print(" Hola", Nom3)
Nota3 = int(input("Agrega tu nota porfavor: "))

if Nota1 < Nota2:
   if Nota1 < Nota3:
        print(" La nota menor la tiene: ", Nom1)
if Nota2 < Nota1:
     if Nota2 < Nota3:
        print(" La nota menor la tiene: ", Nom2)
if Nota3 < Nota2:
   if Nota3 < Nota1:
        print(" La nota menor la tiene: ", Nom3)


if Nota1 > Nota2 and Nota1 > Nota3:
    print(" La nota mayor la tiene: ", Nom1, "con la calificacion de", Nota1)
if Nota2 > Nota1 and Nota2 > Nota3:
    print(" La nota mayor la tiene: ", Nom2, "con la calificacion de", Nota2)
if Nota3 > Nota1 and Nota3 > Nota2:
    print(" La nota mayor la tiene: ", Nom3, "con la calificacion de", Nota3)

if Nota1 == Nota2:
    print(Nom1, "y", Nom2, "Tienen la misma nota")
if Nota1 == Nota3:
    print(Nom1, "y", Nom3, "Tiene la misma nota")
if Nota2 == Nota3:
    print(Nom2, "y", Nom3, "Tiene la misma nota")
if Nota2 == Nota1:
    print(Nom2, "y", Nom1, "Tienen la misma nota")
