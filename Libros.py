D = ("--------------------------------------------------------------------------------------------------------------")
Libros = ["Python", "Don Quijote", "Davinci", "Sherlock Holmes", "Cien años de soledad"]

print("\n**************************************************************************************************************")
print(" La cantidad de elementos de esta lista son:", len(Libros))
print(D)
print(" Lista Original:", Libros)
print(D)
Libros.append( "Test")
print(" Se agrega un nuevo Libro:", Libros)
print(D)
Libros.pop()
print(" Se remueve Libro:", Libros)
print(D)
print(" Se cambia un nuevo Libro:", Libros)
Libros.insert(0, "El señor de los anillos")
# print("**************************************************************************************************************\n")