def calcular_monto_final():
    # Solicitar la cantidad de productos
    cantidad_productos = int(input("Introduce la cantidad de productos: "))
    
    # Solicitar el precio unitario
    precio_unitario = float(input("Introduce el precio unitario del producto: "))
    
    #  Calcular el total sin descuento
    total = cantidad_productos * precio_unitario
    
    #  Calcular el descuento (10%)
    descuento = total * 0.10
    
    #  Calcular el monto final a pagar
    monto_final = total - descuento
    
    # Mostrar el monto final a pagar
    print("El monto final a pagar es:", monto_final)

# Llamar a la función para ejecutar el algoritmo
calcular_monto_final()