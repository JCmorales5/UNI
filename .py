print("\n********************************************")
print("                Registro de datos             ")
print("**********************************************")

#------------------------------------------------------>
# Solicitamos el nombre
Nombre = str(input("Ingrese su nombre:  "))
print("\n--- Bievenido", Nombre, "---")

#------------------------------------------------------>
# Solicitamos edad, peso y altura
Edad = int(input("Ingrese su Edad: ",   ))
Peso = float(input("Ingrese su Peso: ",   ))
Altura = float(input("Ingrese su Altura: ",   ))
mas10 = Edad + 10

#------------------------------------------------------>
# Mostrar los datos
print("--------------------------------------------")
print("Detalles de", Nombre)
print("--------------------------------------------")
print(f"Su edad es de {Edad}\n Su peso es de {Peso}\n Su Altura es de {Altura}")
print(f"{Nombre} en 10 años tendra {mas10}")
print("--------------------------------------------")
