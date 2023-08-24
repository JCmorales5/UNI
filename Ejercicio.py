#print("\033[33m]\033[33m]")
Horas = int(6)
print("\n\033[33m]*****************************************************""\033[33m]")
Nombre = str(input(" ¿Cual es tu nombre?\n"))
print("*****************************************************")
Salario = float(input(f" ¿Cuantos ganas a la semana {Nombre}? \n"))
print("*****************************************************")
Semana = int(input( f" ¿Cuantas días trabajas a la semana {Nombre}? \n"))
print("*****************************************************")
Trabaja_Hora = Horas * Semana
print("*****************************************************")
Hora_ganadas = Salario / Trabaja_Hora
print("*****************************************************")
print(f"Estimado {Nombre} tu horas trabajadas en la semana es de: ", Horas * Semana )
print("*****************************************************")
print(f"Estimado {Nombre} tu ganas por hora: ", Salario / Trabaja_Hora )
print("*****************************************************")


