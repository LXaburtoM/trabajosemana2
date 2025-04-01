Algoritmo calcular_descuento
    Definir cantidad, precioUnitario, total, descuento, totalPagar Como Real
    
    Escribir "Ingrese la cantidad de productos: "
    Leer cantidad
    Escribir "Ingrese el precio unitario del producto: "
    Leer precioUnitario
    
	total <- cantidad * precioUnitario
	descuento <- total * 0.10
	totalPagar <- total - descuento
	
	Escribir "Subtotal: ", total
	Escribir "Descuento aplicado (10%): ", descuento
	Escribir "Total a pagar: ", totalPagar
FinAlgoritmo