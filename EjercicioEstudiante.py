D = ("\n*******************************************************************************************************************************")
A = ("-------------------------------------------------------------------------------------------------------------------------------")
Datos1 = {
    1:{"Nombre1": "JC", "Nombre2": "Alex", "Apellido1": "Jimenez", "Apellido2": "Calero", "Edad": 25 , "Materia": ["Español", "Mate", "Ingles"]},
    2:{"Nombre1": "Carlos", "Nombre2": "Isidro", "Apellido1": "Melendez", "Apellido2": "Perez", "Edad": 35, "Materia": ["Español", "Mate", "Ingles"]},
    3:{"Nombre1": "Mauricio", "Nombre2": "Jesus", "Apellido1": "Suarez", "Apellido2": "Velez", "Edad": 45, "Materia": ["Español", "Mate", "Ingles"]}, 
}


print(D)
print("--- Nombres:", Datos1[1]["Nombre1"], Datos1[1]["Nombre2"], "--- Apellido1:", Datos1[1]["Apellido1"], Datos1[1]["Apellido2"], "--- Edad:", Datos1[3]["Edad"],"--- Materia:", Datos1[3]["Materia"], "---")
print(D)
print("--- Nombres:", Datos1[2]["Nombre1"], Datos1[2]["Nombre2"], "--- Apellido1:", Datos1[2]["Apellido1"], Datos1[2]["Apellido2"], "--- Edad:", Datos1[2]["Edad"],"--- Materia:", Datos1[3]["Materia"], "---")
print(D)
print("--- Nombres:", Datos1[3]["Nombre1"], Datos1[3]["Nombre2"], "--- Apellido1:", Datos1[3]["Apellido1"], Datos1[3]["Apellido2"],  "--- Edad:", Datos1[3]["Edad"],"--- Materia:", Datos1[2]["Materia"], "---")
print(A)
print("\n Modificando el segundo nombre del primer estudiante:")
print(A)
Datos1[1]["Nombre2"] = "Miguel"
print("--- Nombres:", Datos1[1]["Nombre1"], Datos1[1]["Nombre2"], "--- Apellido1:", Datos1[1]["Apellido1"], Datos1[1]["Apellido2"], "--- Edad:", Datos1[3]["Edad"],"--- Materia:", Datos1[3]["Materia"], "---")
print(A)
print("\n Eliminando el segundo apellido del tercer estudiante:")
print(A)
Delerr = Datos1[3].pop("Apellido2")
print("--- Nombres:", Datos1[3]["Nombre1"], Datos1[3]["Nombre2"], "--- Apellido1:", Datos1[3]["Apellido1"], Datos1[3]["Apellido2"],  "--- Edad:", Datos1[3]["Edad"],"--- Materia:", Datos1[2]["Materia"], "---")
print(A)