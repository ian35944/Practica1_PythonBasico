print ("ingrese un nombre del estudiante")
nombre = input()
print ("ingrese el sexo del estudiante ('F' o 'M' )")
sexo = input()
if sexo == "F":
    if nombre.lower()<"m":
        print("Su grupo es el A")
    else:
        print("Su grupo es el B")
else:
    if nombre.lower()<"n":
        print("Su grupo es el A")
    else:
        print("Su grupo es el B")