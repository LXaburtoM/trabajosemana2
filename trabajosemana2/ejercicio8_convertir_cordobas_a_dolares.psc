Algoritmo convertir_cordobas_a_dolares
    Definir dolares, tasaCambio, cordobas Como Real
    
    Escribir "Ingrese la cantidad en cordobas: "
    Leer cordobas
    Escribir "Ingrese el tipo de cambio (1 USD a córdobas): "
    Leer tasaCambio
    
	dolares = cordobas / tasaCambio
	Escribir cordobas, " córdobas equivalen a ", dolares, " dólares."
FinAlgoritmo