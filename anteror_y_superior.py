def antecesor_y_sucesor():
    # Paso 2: Solicitar un número entero
    numero = int(input("Introduce un número entero: "))
    
    # Paso 4: Calcular el antecesor
    antecesor = numero - 1
    
    # Paso 5: Calcular el sucesor
    sucesor = numero + 1
    
    # Paso 6: Mostrar el antecesor y el sucesor
    print("El antecesor de", numero, "es:", antecesor)
    print("El sucesor de", numero, "es:", sucesor)

# Llamar a la función para ejecutar el algoritmo
antecesor_y_sucesor()