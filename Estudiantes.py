print("\033")

print("\n*****************************************************")
print("                  Bienvenido Estudiante                ")
Nombre = str(input(" ¿Cual es tu nombre? "))
Clases_Cursadas = int(input(f" ¿Cuantas clases estas cursando {Nombre }? "))
Clases_Aprobadas = int(input(f" ¿Cuantas clases aprobastes {Nombre} ? "))
Clases_Reprobadas = Clases_Cursadas - Clases_Aprobadas

print(f"El promedio de clases aprobas {Nombre} es de",  Clases_Aprobadas * 100 / Clases_Cursadas, "%")
print(f"El promedio de clases reaprobas {Nombre} es de", Clases_Reprobadas * 100 / Clases_Cursadas, "%")
print("*****************************************************\n")

