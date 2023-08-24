D = ("\n *****************************************************************")
A = ("\n ----------------------------------------------------------------")
print("\n*****************************************************************")
print("                            CALIFICACIONES                         ")
print("\n*****************************************************************")
print(D)
Nom1 = str(input( "Ingrese el Nombre del estudiante1: "))
Esp1 = int(input("Agrega tu nota de Español porfavor: "))
Math1 = int(input("Agrega tu nota de Matematicas porfavor: "))
Ci1 = int(input("Agrega tu nota de Ciencias porfavor: "))
print(D)
Nom2 = str(input( "Ingrese el Nombre del estudiante2: "))
Esp2 = int(input("Agrega tu nota de Español porfavor: "))
Math2 = int(input("Agrega tu nota de Matematicas porfavor: "))
Ci2 = int(input("Agrega tu nota de Ciencias porfavor: "))
print(D)
Nom3 = str(input( "Ingrese el Nombre del estudiante3: "))
Esp3 = int(input("Agrega tu nota de Español porfavor: "))
Math3 = int(input("Agrega tu nota de Matematicas porfavor: "))
Ci3 = int(input("Agrega tu nota de Ciencias porfavor: "))
print(D)
Nom4 = str(input( "Ingrese el Nombre del estudiante4: "))
Esp4 = int(input("Agrega tu nota de Español porfavor: "))
Math4 = int(input("Agrega tu nota de Matematicas porfavor: "))
Ci4 = int(input("Agrega tu nota de Ciencias porfavor: "))
print(D)
Suman1 = Esp1 + Math1 + Ci1
print(A)
Suman2 = Esp2 + Math2 + Ci2
print(A)
Suman3 = Esp3 + Math3 + Ci3
print(A)
Suman4 = Esp4 + Math4 + Ci4
print(A)

print(D)
print("Notas de: ", Nom1, "=" , Suman1)
print(A)
print("Notas de: ", Nom2, "=" , Suman2)
print(A)
print("Notas de: ", Nom3, "=" , Suman3)
print(A)
print("Notas de: ", Nom4, "=" , Suman4)

print(D)
promedio1 = Esp1 + Math1 + Ci1 / 4
print(A)
promedio2 = Esp2 + Math2 + Ci2 / 4
print(A)
promedio3 = Esp3 + Math3 + Ci3 / 4
print(A)
promedio4 = Esp4 + Math4 + Ci4 / 4
print(A)
print(D)
print("Promedio de clases : ", promedio1)
print("Promedio de clases : ", promedio2)
print("Promedio de clases : ", promedio3)
print("Promedio de clases : ", promedio4)
print(D)


if promedio1 > promedio2 and promedio1 > promedio3 and promedio1 > promedio4:
    print(" El promedio mayor lo tiene: ", Nom1, "con la calificacion de", promedio1)
if promedio2 > promedio1 and promedio2 > promedio3 and promedio2 > promedio4:
    print(" El promedio mayor lo tiene: ", Nom2, "con la calificacion de", promedio2)
if promedio3 > promedio1 and promedio3 > promedio2 and promedio3 > promedio4 :
    print(" El promedio mayor lo tiene: ", Nom3, "con la calificacion de", promedio3)
if promedio4 > promedio1 and promedio4 > promedio2 and promedio4 > promedio4 :
    print(" El promedio mayor lo tiene: ", Nom4, "con la calificacion de", promedio4)
print(D)
if promedio1 < promedio2 and promedio1 < promedio3 and promedio1 < promedio4:
    print(" El promedio mayor lo tiene: ", Nom1, "con la calificacion de", promedio1)
if promedio2 < promedio1 and promedio2 < promedio3 and promedio2 < promedio4:
    print(" El promedio mayor lo tiene: ", Nom2, "con la calificacion de", promedio2)
if promedio3 < promedio1 and promedio3 < promedio2 and promedio3 < promedio4 :
    print(" El promedio mayor lo tiene: ", Nom3, "con la calificacion de", promedio3)
if promedio4 < promedio1 and promedio4 < promedio2 and promedio4 < promedio4 :
    print(" El promedio mayor lo tiene: ", Nom4, "con la calificacion de", promedio4)
print(D)
if promedio1 == promedio2:
    print(Nom1, "y", Nom2, "Tienen la misma nota")
    if promedio1 == promedio3:
        print(Nom1, "y", Nom3, "Tiene la misma nota")
        if promedio1 == promedio4:
            print(Nom1, "y", Nom4, "Tiene la misma nota")
if promedio2 == promedio1:
    print(Nom1, "y", Nom2, "Tienen la misma nota")
    if promedio2 == promedio3:
        print(Nom2, "y", Nom3, "Tiene la misma nota")
        if promedio2 == promedio4:
            print(Nom3, "y", Nom4, "Tiene la misma nota")
if promedio3 == promedio1:
    print(Nom1, "y", Nom2, "Tienen la misma nota")
    if promedio3 == promedio2:
        print(Nom2, "y", Nom3, "Tiene la misma nota")
        if promedio3 == promedio4:
            print(Nom3, "y", Nom4, "Tiene la misma nota")     
if promedio4 == promedio1:
    print(Nom1, "y", Nom2, "Tienen la misma nota")
    if promedio4 == promedio2:
        print(Nom2, "y", Nom3, "Tiene la misma nota")
        if promedio4 == promedio3:
            print(Nom3, "y", Nom4, "Tiene la misma nota")      