def convertir_dolares_a_cordobas():
    #  Solicitar la cantidad en dólares
    dolares = float(input("Introduce la cantidad en dólares: "))
    # Definir el tipo de cambio fijo
    tipo_cambio = 36.60
    #  Calcular la cantidad en córdobas
    cordobas = dolares * tipo_cambio
    #ostrar la cantidad en córdobas
    print(f"La cantidad en córdobas es: {cordobas:.2f}")
# Llamar a la función para ejecutar el algoritmo
convertir_dolares_a_cordobas()