def calcular_nota_final():
    # Definir las variables
    nota1 = int(input("Introduzca la nota 1: "))
    nota2 = int(input("Introduzca la nota 2: "))
    nota3 = int(input("Introduzca la nota 3: "))
    nota4 = int(input("Introduzca la nota 4: "))
    nota5 = int(input("Introduzca la nota 5: "))
    # Calcular la nota final
    nota_final = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    # Redondear la nota final
    print("La nota final es:", nota_final)
# Llamar a la función para ejecutar el algoritmo
calcular_nota_final()